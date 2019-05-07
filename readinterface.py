'''
接口文件中需要考虑2点。1、文件中包含2个部分。第一部分，以[业务说明]开头，是本api文档的组织说明，调用之间的依赖等。这个部分由开发人员编写，是设计测试数据的基础。第二部分以开头[API说明]是具体的api说明。2、入库。每次有新增的api都需要全量的读入，稳定的api需要保留在数据库中。
'''
import re
import dbapi

### api文件分为结构和api2个部分
filename = 'aaa.txt'
testname = 'aaa.txt'
struct = ''
apis=''

### 读取文件
#file1 = open(filename,"r")
file1 = open(testname,"r")
str1 = file1.read()

struct, apis=str1.split('[API说明]')

### 处理api组织
# 检查测试用例是否全覆盖
# JSON表示层级关系，去掉前面的数字，后面再重新进行编码。如"调拨流程":{"调拨单操作":{"创建调拨单":{"获取登录用户可以调拨的仓库":"叶子节点内容"}},"调拨单明细操作":}

list1=re.split('((?:[0-9]+\.)+[0-9]*)',str1)
list1.pop(0)


### 处理api
# 检查测试用例的是否正确
apikeys=[]
apivalues=[]
# 获取ID
#findall返回最短值，finditer返回最长的值，如第一条结果对应为"1.1"和"1.1.1"。"坑“
#apikeys = listre.findall(r'(^[0-9]\.+[0-9])',  apis, re.M)
api1 = re.finditer(r'([0-9]+\.)+[0-9]+',  apis, re.M)
for aa in api1:
	apikeys.append(aa.group())

#获取json内容
apivalues = re.split('(?:[0-9]+\.)+[0-9]+', apis)
# 去掉list中的第一个空对象
apivalues.pop(0)
# utf8格式中，汉字为3个ASCII字符。去掉所有的空格(ASCII值为20)和tab键(ASCII值为09)，tab一般会变成多个空格。
# 将中文的：替换为英文的:,将空格去掉，将行首的回车“^\n”替换为“”。
# 各种去掉\n。

list1=apivalues;

trans1=[('：',':'),(' ',''),('^\n',''),('(\n)+','\n'),('\n}','}'),('\n{','{'),('{\n','{'),('}\n','}'),('\n\[','['),('\n\]',']'),('\[\n','['),('\]\n',']'),(',\n',','),('\n',','),('返回数据',',返回数据')]
for o1,t1 in trans1:
	values_map = map(lambda _:re.sub(o1,t1,_,0,0),list1)
	list1=list(values_map)

### 写入数据库
# 建库表
dbname = './interface.db'
innertable = 'innerinterface'
createinnertable = 'create table ' + innertable + '(key int(10) primary key  NOT NULL, value JSON  NOT NULL)'
insertdata = 'insert into `'+ innertable + '` values (?,?)'
innerdata = []
for d1 in range(len(apikeys)):
	innerdata.append((apikeys[d1], list1[d1]))

# 写入数据库
conn = dbapi.get_conn(dbname)
dbapi.drop_table(conn, innertable)
conn = dbapi.get_conn(dbname)
dbapi.create_table(conn, createinnertable)
conn = dbapi.get_conn(dbname)
dbapi.save(conn, insertdata,innerdata)

#建立库表
#将接口文件写入到数据库中
#以上为一个文件

#建立案例表
#一个独立的文件处理

#测试
#一个独立的文件处理.
