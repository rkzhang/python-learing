#-*-coding:UTF-8-*-
'''
Created on 2016年7月14日

@author: rkzhang
'''
import xlrd
import uuid
from _sqlite3 import Row
from dao.data_source import getConn, getCur
import random

def main() :
    school_list = getAllSchool()
    
    wares_list = getAllWares();
    for ware in wares_list : 
        print ware;
    
    for school in school_list :
        print school
        supplier_list = getSupplierBySchoolId(school['id'])
        for supplier in supplier_list :
            print "supplier ----- " + str(supplier)
            users_list = getUsersBySupplierId(supplier['id'])
            if users_list == None :
                continue
            for user in users_list :
                print "user ***** " + str(user)
                
                warelist = random.sample(wares_list, 10)
                mastId = uuid.uuid4()
                saveLedgerMaster(school, supplier, user)
                for(ware in warelist) :
                    saveLedger(school, supplier, user, ware)
                
def saveLedgerMaster(school, supplier, user) :
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "insert into t_edu_school(id, school_name, longitude, latitude, level, address_code, index_key, create_time, stat) values('%s','%s','%f','%f','%d','%s','%s',now(), 1)" % (uuid.uuid4(), record['schoolName'], record['x'], record['y'], record['schoolLevel'], record['schoolDistrict'], record['indexKey'])
                print sql
                cur.execute(sql)  
            except Exception, cc :
                print cc

def saveLedger(school, supplier, user, ware) :
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "insert into t_edu_school(id, school_name, longitude, latitude, level, address_code, index_key, create_time, stat) values('%s','%s','%f','%f','%d','%s','%s',now(), 1)" % (uuid.uuid4(), record['schoolName'], record['x'], record['y'], record['schoolLevel'], record['schoolDistrict'], record['indexKey'])
                print sql
                cur.execute(sql)  
            except Exception, cc :
                print cc
                
def getAllWares() : 
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "select * from t_pro_wares ware where stat=1" 
                print sql
                cur.execute(sql)  
                
                rows =cur.fetchall()  
                wares_list = []
                for row in rows:  
                    ware = {}
                    ware['id'] = row[0] 
                    ware['wares_name'] = row[1]
                    ware['spec'] = row[2] 
                    ware['amount_unit'] = row[3]
                    ware['shelf_life'] = row[4]
                    ware['unit'] = row[5]
                    ware['supplier_id'] = row[6]
                    ware['way'] = row[7]
                    ware['wares_type'] = row[8]
                    ware['custom_code'] = row[9]
                    ware['image'] = row[10]
                    ware['manufacturer'] = row[11]
                    ware['bar_code'] = row[12]
                    ware['en_name'] = row[13]
                    ware['place'] = row[14]
                    ware['dishes'] = row[15]
                    ware['remark'] = row[16]
                    ware['creator'] = row[17]
                    ware['create_time'] = row[18] 
                    ware['updater'] = row[19]
                    ware['last_update_time'] = row[20]
                    ware['stat'] = row[21]
                   
                    wares_list.append(ware)
                return wares_list
            except Exception, cc :
                print cc

def getUsersBySupplierId(supplierId) :
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "select * from t_pro_users users where stat=1 and isAdmin=0 and source_id='%s'" % (supplierId) 
                print sql
                cur.execute(sql)  
                
                rows =cur.fetchall()  
                users_list = []
                for row in rows:  
                    user = {}
                    user['id'] = row[0]
                    user['age'] = row[1]
                    user['source_id'] = row[2]
                    user['email'] = row[3]
                    user['gender'] = row[4]
                    user['isAdmin'] = row[5]
                    user['name'] = row[6]
                    user['pj_no'] = row[7]
                    user['post_no'] = row[8]
                    user['password'] = row[9]
                    user['qjy_account'] = row[10]
                    user['user_account'] = row[11] 
                    user['user_image'] = row[12]
                    user['user_no'] = row[13]
                    user['user_type'] = row[14]
                    user['creator'] = row[15]
                    user['create_time'] = row[16]
                    user['updater'] = row[17]
                    user['last_update_time'] = row[18]
                    user['stat'] = row[19]
                   
                    users_list.append(user)
                return users_list
            except Exception, cc :
                print cc
    


def getSupplierBySchoolId(schoolId) : 
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "select * from  t_pro_supplier sup LEFT JOIN t_edu_school_supplier map on sup.id = map.supplier_id and map.stat = 1 LEFT JOIN t_edu_school school on school.id = map.school_id and school.stat = 1 where sup.stat = 1 and school_id = '%s'" % (schoolId) 
                print sql
                cur.execute(sql)  
                
                rows =cur.fetchall()  
                supplier_list = []
                for row in rows:  
                    supplier = {}
                    supplier['id'] = row[0]
                    supplier['supplier_name'] = row[1]
                    supplier['address'] = row[2]
                    supplier['provinces'] = row[3]
                    supplier['city'] = row[4]
                    supplier['area'] = row[5]
                    supplier['supplier_type'] = row[6]
                    supplier['business_license'] = row[7]
                    supplier['organization_code'] = row[8]
                    supplier['food_service_code'] = row[9]
                    supplier['food_service_code_date'] = row[10]
                    supplier['food_business_code'] = row[11]
                    supplier['food_business_code_date'] = row[12]
                    supplier['food_circulation_code'] = row[13]
                    supplier['food_circulation_code_date'] = row[14]
                    supplier['food_produce_code'] = row[15]
                    supplier['food_produce_code_date'] = row[16]
                    supplier['corporation'] = row[17]
                    supplier['id_card'] = row[18]
                    supplier['id_type'] = row[19]
                    supplier['contact_way'] = row[20]
                    supplier['longitude'] = row[21]
                    supplier['latitude'] = row[22]
                    supplier['reviewed'] = row[23]
                    supplier['create_time'] = row[24]
                    supplier['updater'] = row[25]
                    supplier['last_update_time'] = row[26]
                    supplier['stat'] = row[27]
                   
                    supplier_list.append(supplier)
                return supplier_list
            except Exception, cc :
                print cc

def getAllSchool() :
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "select * from t_edu_school where stat=1" 
                print sql
                cur.execute(sql)  
                
                rows =cur.fetchall()  
                school_list = []
                for row in rows:  
                    school = {}
                    school['id'] = row[0]
                    school['committee_id'] = row[1]
                    school['school_name'] = row[2]
                    school['school_thum'] = row[3]
                    school['mobile_no'] = row[4]
                    school['contacts'] = row[5]
                    school['address'] = row[6]
                    school['longitude'] = row[7]
                    school['latitude'] = row[8]
                    school['level'] = row[9]
                    school['supplier_id'] = row[10]
                    school['reviewed'] = row[11]
                    school['create_time'] = row[12]
                    school['updater'] = row[13]
                    school['last_update_time'] = row[14]
                    school['stat'] = row[15]
                    school_list.append(school)
                return school_list
            except Exception, cc :
                print cc


if __name__ == '__main__':
    main()