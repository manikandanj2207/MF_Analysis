# -*- coding: utf-8 -*-

from lxml import html  
import requests
import csv
from time import sleep

def ParseReviews(asin, num_of_pages):
    
                reviews_overall = {}
	
           	for i in range(num_of_pages):
           	    
         			#amazon_url  = 'http://www.amazon.com/dp/'+asin  # <---- To collect the product details - Not required 
         			#amazon_url  = 'https://www.amazon.com/product-reviews/' + asin + '/ref=cm_cr_arp_d_paging_btm_3?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=3' # <---- To collect the average reviews
         			#amazon_url  = 'https://www.amazon.com/product-reviews/' + asin + '/ref=cm_cr_getr_d_paging_btm_3?ie=UTF8&reviewerType=all_reviews&pageNumber=3'  # <---- To collect all the reviews
         			amazon_url   = 'https://www.amazon.com/product-reviews/' + asin + '/ref=cm_cr_getr_d_paging_btm_'+ str(i+1) + '?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(i+1)  # <---- To collect all the reviews
         			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
                                
                                print "Iteration # : ", i+1      			
         			print "I am feeling sleepy"
         			sleep(20)    # Respect the Amazon TOS and do not over pull data
         			print "I am awake, I am awake"
         			print "Extracting data from url : ", amazon_url
         			
         			page = requests.get(amazon_url,headers = headers)
         			page_response = page.text
            
         			parser = html.fromstring(page_response)
         			XPATH_REVIEW_SECTION_2 = '//div[@data-hook="review"]'
         			XPATH_AGGREGATE_RATING = '//table[@id="histogramTable"]//tr'
         			XPATH_PRODUCT_NAME = '//h1//span[@id="productTitle"]//text()'
         			XPATH_PRODUCT_PRICE  = '//span[@id="priceblock_ourprice"]/text()'
         			
         			raw_product_price = parser.xpath(XPATH_PRODUCT_PRICE)
         			product_price = ''.join(raw_product_price).replace(',','')
            
         			raw_product_name = parser.xpath(XPATH_PRODUCT_NAME)
         			product_name = ''.join(raw_product_name).strip()
         			
         			total_ratings  = parser.xpath(XPATH_AGGREGATE_RATING)
            
         			reviews = parser.xpath(XPATH_REVIEW_SECTION_2)
         			
         			#print reviews[0]
         			
         			ratings_dict = {}
         			#reviews_dict = {}
         			
         			if not reviews:
            				raise ValueError('unable to find reviews in page')
            
         			#grabing the rating  section in product page
         			for ratings in total_ratings:
            				extracted_rating = ratings.xpath('./td//a//text()')
            				if extracted_rating:
           					rating_key = extracted_rating[0] 
           					raw_raing_value = extracted_rating[1]
           					rating_value = raw_raing_value
           					if rating_key:
          						ratings_dict.update({rating_key:rating_value})

                                review_counter = i * 10  # Assuming 10 reviews per page; Correct index if this is not true
                                
         			#Parsing individual reviews
         			for review in reviews:
         			    
              		                    raw_review_stars = ''
                                            raw_review_purchase = ''
                                            raw_review_title1 = ''
                                            raw_review_author = ''
                                            raw_review_date = '' 
                                            raw_review_productpackage = ''
                                            raw_review_text = ''
                                            raw_review_comments_details = '' 
                                            
                                            for i in review.iterchildren():
                                                for j in i.iterchildren():
                                                    for k in j.iterchildren():
                                                        #print k.attrib
                                                        #print k.attrib.keys()
                                                        
                                                        if 'title' in k.attrib.keys():
                                                            raw_review_stars = k.text_content()
                                                            
                                                        if 'data-action' in k.attrib.keys():
                                                            raw_review_purchase = k.text_content()
                                                                
                                                        if 'data-hook' in k.attrib.keys():
                                                            if k.attrib['data-hook'] == 'review-title':
                                                                raw_review_title1 = k.text_content()
                                            
                                                            if k.attrib['data-hook'] == 'review-author':         
                                                                for m in k.getiterator():
                                                                    if 'data-hook' in m.attrib.keys():
                                                                        if m.text_content()[:2] != 'By' :
                                                                            raw_review_author =  m.text_content()
                                                                    
                                                            if k.attrib['data-hook'] == 'review-date':         
                                                                for m in k.getiterator():
                                                                    if 'data-hook' in m.attrib.keys():
                                                                        #if m.text_content()[:2] != 'By' :
                                                                        raw_review_date =  m.text_content()
                                                                            
                                                            if k.attrib['data-hook'] == 'format-strip':         
                                                                for m in k.getiterator():
                                                                            #print  m.attrib
                                                                        raw_review_productpackage =  m.text_content()
                                                        
                                                            if k.attrib['data-hook'] == 'review-body':       
                                                                #print "****************** Line Separator ******************"  
                                                                raw_review_text = ''
                                                                for m in k.getiterator():
                                                                        if m.text_content() != ' ' :
                                                                            raw_review_text = raw_review_text + ' ' + m.text_content()  
                                                                raw_review_text = raw_review_text.strip()
                                                                            
                                                        if 'data-reftag' in k.attrib.keys():
                                                            #print "I was here :-)"
                                                            raw_review_comments_details =  k.text_content().split('.')[0] 
                                            
            
            				
            			            reviews_overall[review_counter] = {
           	    								    'raw_review_stars' : raw_review_stars, 
                                                                                    'raw_review_purchase' : raw_review_purchase,
                                                                                    'raw_review_title1' : raw_review_title1,
                                                                                    'raw_review_author' : raw_review_author,
                                                                                    'raw_review_date' : raw_review_date, 
                                                                                    'raw_review_productpackage' : raw_review_productpackage,
                                                                                    'raw_review_text' : raw_review_text,
                                                                                    'raw_review_comments_details' : raw_review_comments_details
            								   }
            				    review_counter += 1
            												
            
         	data = {
          						'ratings':ratings_dict,
          						'reviews':reviews_overall,
          						'url':amazon_url,
          						'price':product_price,
          						'name':product_name
           	       }
           	       
         	return data
          		
          		

	#Add your own ASINs here; One at a time
#AsinList = ['B00DW1JT5G',]
AsinList = ['B01IK52REI',]
num_of_pages_to_be_extracted = 5    # Number of pages and each page will include 10 reviews 

Data_out = ParseReviews(AsinList[0],num_of_pages_to_be_extracted)

with open('D:/Users/Desktop/Amazon_reviews/B01IK52REI_reviews.csv','wb') as csv_file:  # <----- Change filename for new ASIN
    writer = csv.writer(csv_file)
    csv_header = 'raw_review_stars,raw_review_purchase,raw_review_title1,raw_review_author,raw_review_date,raw_review_productpackage,raw_review_text,raw_review_comments_details'
    writer.writerow([csv_header])
    for key in Data_out['reviews'].keys():
        str_temp = '"'
        str_temp = str_temp + Data_out['reviews'][key]['raw_review_stars'].replace(',',' ') + '"' 
        str_temp = str_temp + ',"' + Data_out['reviews'][key]['raw_review_purchase'].replace(',',' ') + '"'
        str_temp = str_temp + ',"' + Data_out['reviews'][key]['raw_review_title1'].replace(',',' ') + '"'
        str_temp = str_temp + ',"' + Data_out['reviews'][key]['raw_review_author'].replace(',',' ') + '"'
        str_temp = str_temp + ',"' + Data_out['reviews'][key]['raw_review_date'].replace(',',' ') + '"'
        str_temp = str_temp + ',"' + Data_out['reviews'][key]['raw_review_productpackage'].replace(',',' ') + '"'
        str_temp = str_temp + ',"' + Data_out['reviews'][key]['raw_review_text'].replace(',',' ') + '"'
        str_temp = str_temp + ',"' + Data_out['reviews'][key]['raw_review_comments_details'].replace(',',' ') + '"'
        
        writer.writerow([str_temp.encode('utf-8')])
