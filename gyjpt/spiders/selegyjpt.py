# -*- coding: utf-8 -*-
from gyjpt.items import GyjptItem
from selenium import webdriver
import time
import cx_Oracle
browser=webdriver.Firefox()
browser.get("http://www.gdyjs.cn/UserService/ProductList.aspx")

def conect_oracle():
    conn = cx_Oracle.connect("hyspd/1@localhost:1521/spd")
    cursor=conn.cursor()
    return cursor,conn

def get_one():
 elemnt=browser.find_element_by_xpath("//table[@align='center']").find_elements_by_tag_name("tr")
 sql="insert into gyj_product (protduct_name,goods_name,product_location,product_xin,product_desc) values ('%s','%s','%s','%s','%s')"
 try:
  for i in elemnt:
    g=GyjptItem()
    c=i.find_elements_by_tag_name("td")
    cursor.execute(sql %(c[0].text,c[1].text,c[2].text,c[3].text,c[4].text))
    conn.commit()
 except :
    pass





def print_it(pro_mu):
    for i in pro_mu:
        print i['protduct_name'],i['goods_name'],i['product_location'],i['product_xing'],i['product_desc']

def get_all(a_page,cursor,conn):
    cur_no=1
    for i in range(1,a_page):
        next_page = browser.find_element_by_link_text("下一页")
        get_one()
        next_page.click()
        time.sleep(5)






cursor,conn=conect_oracle()
get_all(2156,cursor,conn)







