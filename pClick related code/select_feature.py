import sys
from pyspark import SparkContext

def process_query(query):
    fields = query.split(" ")
    output = "_".join(fields)
    return output

#Device IP: field[0]
# Device id: field[1]
#Session id: field[2]
#Query: field[3] txt
#AdId : field[4]
#CampaignId : field[5]
#Ad_category_Query_category(0/1) : field[6]
#clicked(0/1) : field[7]

if __name__ == "__main__":
    file = sys.argv[1] #raw search log
    sc = SparkContext(appName="CTR_Features")
    output_dir = "/Users/mac/project/SearchAds/data/log/"
    data = sc.textFile(file).map(lambda line: line.encode("utf8", "ignore").split(','))
    #count feature
    device_ip_click = data.map(lambda fields: (fields[0],int(fields[7]))).reduceByKey(lambda v1,v2: v1+v2)
    device_ip_impression = data.map(lambda fields: (fields[0],1)).reduceByKey(lambda v1,v2: v1+v2)

    device_id_click = data.map(lambda fields: (fields[1],int(fields[7]))).reduceByKey(lambda v1,v2: v1+v2)
    device_id_impression = data.map(lambda fields: (fields[1],1)).reduceByKey(lambda v1,v2: v1+v2)

    ad_id_click = data.map(lambda fields: (fields[4],int(fields[7]))).reduceByKey(lambda v1,v2: v1+v2)
    ad_id_impression = data.map(lambda fields: (fields[4],1)).reduceByKey(lambda v1,v2: v1+v2)

    query_campaign_id_click = data.map(lambda fields: (process_query(fields[3]) + "_" + fields[5],int(fields[7]))).reduceByKey(lambda v1,v2: v1+v2)
    query_campaign_id_impression = data.map(lambda fields: (process_query(fields[3]) + "_" + fields[5],1)).reduceByKey(lambda v1,v2: v1+v2)

    query_ad_id_click = data.map(lambda fields: (process_query(fields[3]) + "_" + fields[4],int(fields[7]))).reduceByKey(lambda v1,v2: v1+v2)
    query_ad_id_impression = data.map(lambda fields: (process_query(fields[3]) + "_" + fields[4],1)).reduceByKey(lambda v1,v2: v1+v2)

    device_id_click.saveAsTextFile(output_dir + "demo_device_id_click")
    device_id_impression.saveAsTextFile(output_dir + "demo_device_id_impression")

    device_ip_click.saveAsTextFile(output_dir + "demo_device_ip_click")
    device_ip_impression.saveAsTextFile(output_dir + "demo_device_ip_impression")

    ad_id_click.saveAsTextFile(output_dir + "demo_ad_id_click")
    ad_id_impression.saveAsTextFile(output_dir + "demo_ad_id_impression")

    query_campaign_id_click.saveAsTextFile(output_dir + "demo_query_campaign_id_click")
    query_campaign_id_impression.saveAsTextFile(output_dir + "demo_query_campaign_id_impression")

    query_ad_id_click.saveAsTextFile(output_dir + "demo_query_ad_id_click")
    query_ad_id_impression.saveAsTextFile(output_dir +"demo_query_ad_id_impression")
    sc.stop()
