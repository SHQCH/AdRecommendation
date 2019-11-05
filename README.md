## Ad Recommendation System
# WebCrawler
The adds data are faked by web crawling amazon.com
Ads data prepared in Json

# SearchAds
1. Build an Ad forward-indexing search engine, save structured Ad data into mySQL
2. Build an Ad invert-indexing search engine using memcached. key = Ad keyword, value = AdID
3. Create a web server to take http query, parse query into keywords, query search engine, return list of AdIDs, that match with query keywords.

# p_click related code
1. prepare ML training data, features are count-based data, use Spark to count number of clicks under each AdID, IP, Category, DeviceID,..
   label: click/not Click
2. train machine learning models (lr, and gbdt)
3. predict Ad click-through-rate (CTR), score and ranking Ads
