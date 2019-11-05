package java.mac.model;

import java.io.Serializable;
import java.util.List;


public class Ad implements Serializable{
    /**
     * created by Jingang Liu (GATECH) 2018
     */
    private static final long serialVersionUID = 1L;
    public int adId;
    public int campaignId;  // from rawQuery data
    public List<String> keyWords;
    public double relevanceScore;
    public double pClick;
    public double bidPrice;    // from rawQuery data
    public double rankScore;
    public double qualityScore;
    public double costPerClick;
    public int position;//1: top , 2: bottom
    public String title; // required
    public double price; // required
    public String thumbnail; // required
    public String description; // required
    public String brand; // required
    public String detail_url; // required
    public String query; //required    // from rawQuery data
    public int query_group_id;         // from rawQuery data
    public String category;
}