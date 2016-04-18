#-*-coding:UTF-8-*-
'''
Created on 2016年4月11日

@author: Administrator
'''
import xlrd
import uuid
from _sqlite3 import Row
from dao.data_source import getConn, getCur
import random

def main() :
    area = {
        '上海市' : '310000',
        '崇明县' : '310230',
        '吴淞区' : '310112',
        '嘉定区' : '310115',
        '南市区' : '310103',
        '青浦区' : '310119',
        '宝山区' : '310114',
        '长宁区' : '310106',
        '奉贤区' : '310226',
        '静安区' : '310107',
        '浦东新区' : '310116',
        '南汇区' : '310225',
        '闸北区' : '310109',
        '杨浦区' : '310111',
        '闵行区' : '310113',
        '徐汇区' : '310105',
        '松江区' : '310118',
        '普陀区' : '310108',
        '虹口区' : '310110',
        '卢湾区' : '310104',
        '黄浦区' : '310101',
        '金山区' : '310117'
    }
    
    levels = {
        '幼儿园' : 0,
        '小学' : 1,
        '中学' : 2     
    }
    
    # 打开文件
    workbook = xlrd.open_workbook(r'D:/school.xlsx')
    
    # 获取所有sheet
    print workbook.sheet_names()[0]
    
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)
    
    nrows = sheet1.nrows #行数
    ncols = sheet1.ncols #列数

    print nrows, ncols
    
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S','T','U','V','W','X','Y','Z']
    
    suppliers = ['562895c6-f29c-4733-8ca5-0db6394dcdef', '6e75ffc3-b980-4f9f-b565-ab9991e55c5b', 'e0a1d71f-5d74-4db9-8b8d-65374da52ee5']
    
    schoolDistrict = ''
    schoolLevel = '';
    for rownum in range(1, 343):
        record = {}      
        record['districtName'] = sheet1.cell(rownum, 0).value.encode('utf-8')
        record['schoolLevel'] = sheet1.cell(rownum, 2).value
        record['schoolName'] = sheet1.cell(rownum, 4).value.encode('utf-8')
        record['coordinate'] = sheet1.cell(rownum, 5).value
        record['indexKey'] = random.choice(list)
        
        districtCoordinat = sheet1.cell(rownum, 1).value
        
        if(record['schoolName'].strip() == '') :
            continue
        
        if(record['districtName'].strip() != '') : 
            schoolDistrict = record['districtName']
            
        if(record['schoolLevel'].strip() != '') : 
            schoolLevel = record['schoolLevel']
        
        record['schoolDistrict'] = area.get(schoolDistrict)
        record['schoolLevel'] = levels.get(schoolLevel.encode('utf-8'))
        
        if(record['coordinate'] != '') : 
            coordinate_split = record['coordinate'].split(',')
            record['x'] = float(coordinate_split[0])
            record['y'] = float(coordinate_split[1])
        print record
        save(record)
        
def save(record) :
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "insert into t_edu_school(id, school_name, longitude, latitude, level, address_code, index_key, create_time, stat) values('%s','%s','%f','%f','%d','%s','%s',now(), 1)" % (uuid.uuid4(), record['schoolName'], record['x'], record['y'], record['schoolLevel'], record['schoolDistrict'], record['indexKey'])
                print sql
                cur.execute(sql)  
            except Exception, cc :
                print cc

if __name__ == '__main__':
    main()