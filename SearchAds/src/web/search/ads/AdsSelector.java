package web.search.ads;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

import net.spy.memcached.MemcachedClient;
public class AdsSelector {
	private static AdsSelector instance = null;
	//private int EXP = 7200;
	private String mMemcachedServer;
	private int mMemcachedPortal;
	private String mysql_host;
	private String mysql_db;
	private String mysql_user;
	private String mysql_pass;
	protected AdsSelector(String memcachedServer,int memcachedPortal,String mysqlHost,String mysqlDb,String user,String pass)
	{
		mMemcachedServer = memcachedServer;
		mMemcachedPortal = memcachedPortal;	
		mysql_host = mysqlHost;
		mysql_db = mysqlDb;	
		mysql_user = user;
		mysql_pass = pass;
	}
	public static AdsSelector getInstance(String memcachedServer,int memcachedPortal,String mysqlHost,String mysqlDb,String user,String pass) {
	      if(instance == null) {
	         instance = new AdsSelector(memcachedServer, memcachedPortal,mysqlHost,mysqlDb,user,pass);
	      }
	      return instance;
    }
	public List<Ad> selectAds(List<String> queryTerms)
	{
		List<Ad> adList = new ArrayList<Ad>();
		HashMap<Long,Integer> matchedAds = new HashMap<Long,Integer>();
		try {
			MemcachedClient cache = new MemcachedClient(new InetSocketAddress(mMemcachedServer,mMemcachedPortal));

			for(String queryTerm : queryTerms)
			{
				System.out.println("selectAds queryTerm = " + queryTerm);
				@SuppressWarnings("unchecked")
				Set<Long>  adIdList = (Set<Long>)cache.get(queryTerm);
				if(adIdList != null && adIdList.size() > 0)
				{
					for(Object adId : adIdList)
					{
						Long key = (Long)adId;
						if(matchedAds.containsKey(key)) // matchedAds, save <AdID: counts that matched>
						{
							int count = matchedAds.get(key) + 1;
							matchedAds.put(key, count);
						}
						else
						{
							matchedAds.put(key, 1);
						}
					}
				}				
			}
			for(Long adId:matchedAds.keySet())
			{			
				System.out.println("selectAds adId = " + adId);
				MySQLAccess mysql = new MySQLAccess(mysql_host, mysql_db, mysql_user, mysql_pass);
				Ad  ad = mysql.getAdData(adId);
				double relevanceScore = (double) (matchedAds.get(adId) * 1.0 / ad.keyWords.size());
				ad.relevanceScore = relevanceScore;
				System.out.println("selectAds pClick = " + ad.pClick);
				System.out.println("selectAds relevanceScore = " + ad.relevanceScore);
				adList.add(ad);
			}			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return adList;
	}
}
