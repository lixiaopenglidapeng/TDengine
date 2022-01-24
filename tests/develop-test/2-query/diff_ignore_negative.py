import sys 
from util.log import *
from util.cases import *
from util.sql import *

class TDTestCase:
    def caseDescription(self):
        '''
        case1<shenglian zhou>: [TD-11204]Difference improvement that can ignore negative 
        ''' 
        return
    
    def init(self, conn, logSql):
        tdLog.debug("start to execute %s" % __file__)
        tdSql.init(conn.cursor(), logSql)
        self._conn = conn

    def run(self):
        print("running {}".format(__file__))
        tdSql.execute("drop database if exists diffneg")
        tdSql.execute("create database if not exists diffneg")
        tdSql.execute('use diffneg')
        tdSql.execute('create table st(ts timestamp, c1 int, c2 float) tags(t int);')

        tdSql.execute('create table ct1 using st tags(1);')

        tdSql.execute('create table ct2 using st tags(2);')

        tdSql.execute('insert into ct1 values(1642662622000, 1, 2)(1642662622001, 2, 4)(1642662622003, -4, -6)(1642662622004, 4, 8);')

        tdSql.execute('insert into ct2 values(1642662622001, 11, 22)(1642662622002, 22, 44)(1642662622003, -44, -66) (1642662622004, 44, 88);')

        tdSql.query('select diff(c1) from st group by tbname')
        tdSql.checkRows(6)
        tdSql.checkData(0, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 1000))
        tdSql.checkData(0, 1, 1)
        tdSql.checkData(0, 2, 'ct1')
        tdSql.checkData(1, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(1, 1, -6)
        tdSql.checkData(1, 2, 'ct1')
        tdSql.checkData(2, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(2, 1, 8)
        tdSql.checkData(2, 2, 'ct1')
        tdSql.checkData(3, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 2000))
        tdSql.checkData(3, 1, 11)
        tdSql.checkData(3, 2, 'ct2')
        tdSql.checkData(4, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(4, 1, -66)
        tdSql.checkData(4, 2, 'ct2')
        tdSql.checkData(5, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(5, 1, 88)
        tdSql.checkData(5, 2, 'ct2')

        tdSql.query('select diff(c1,0) from st group by tbname')
        tdSql.checkRows(6)
        tdSql.checkData(0, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 1000))
        tdSql.checkData(0, 1, 1)
        tdSql.checkData(0, 2, 'ct1')
        tdSql.checkData(1, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(1, 1, -6)
        tdSql.checkData(1, 2, 'ct1')
        tdSql.checkData(2, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(2, 1, 8)
        tdSql.checkData(2, 2, 'ct1')
        tdSql.checkData(3, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 2000))
        tdSql.checkData(3, 1, 11)
        tdSql.checkData(3, 2, 'ct2')
        tdSql.checkData(4, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(4, 1, -66)
        tdSql.checkData(4, 2, 'ct2')
        tdSql.checkData(5, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(5, 1, 88)
        tdSql.checkData(5, 2, 'ct2')

        tdSql.query('select diff(c1,1) from st group by tbname')
        tdSql.checkRows(4)
        tdSql.checkData(0, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 1000))
        tdSql.checkData(0, 1, 1)
        tdSql.checkData(0, 2, 'ct1')
        tdSql.checkData(1, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(1, 1, 2)
        tdSql.checkData(1, 2, 'ct1')
        tdSql.checkData(2, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 2000))
        tdSql.checkData(2, 1, 11)
        tdSql.checkData(2, 2, 'ct2')
        tdSql.checkData(3, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(3, 1, 22)
        tdSql.checkData(3, 2, 'ct2')

        tdSql.query('select diff(c2) from st group by tbname')
        tdSql.checkRows(6)
        tdSql.checkData(0, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 1000))
        tdSql.checkData(0, 1, 2.0)
        tdSql.checkData(0, 2, 'ct1')
        tdSql.checkData(1, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(1, 1, -10.0)
        tdSql.checkData(1, 2, 'ct1')
        tdSql.checkData(2, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(2, 1, 14.0)
        tdSql.checkData(2, 2, 'ct1')
        tdSql.checkData(3, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 2000))
        tdSql.checkData(3, 1, 22.0)
        tdSql.checkData(3, 2, 'ct2')
        tdSql.checkData(4, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(4, 1, -110.0)
        tdSql.checkData(4, 2, 'ct2')
        tdSql.checkData(5, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(5, 1, 154.0)
        tdSql.checkData(5, 2, 'ct2')

        tdSql.query('select diff(c2,0) from st group by tbname')
        tdSql.checkRows(6)
        tdSql.checkData(0, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 1000))
        tdSql.checkData(0, 1, 2.0)
        tdSql.checkData(0, 2, 'ct1')
        tdSql.checkData(1, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(1, 1, -10.0)
        tdSql.checkData(1, 2, 'ct1')
        tdSql.checkData(2, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(2, 1, 14.0)
        tdSql.checkData(2, 2, 'ct1')
        tdSql.checkData(3, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 2000))
        tdSql.checkData(3, 1, 22.0)
        tdSql.checkData(3, 2, 'ct2')
        tdSql.checkData(4, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 3000))
        tdSql.checkData(4, 1, -110.0)
        tdSql.checkData(4, 2, 'ct2')
        tdSql.checkData(5, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(5, 1, 154.0)
        tdSql.checkData(5, 2, 'ct2')

        tdSql.query('select diff(c2,1) from st group by tbname')
        tdSql.checkRows(4)
        tdSql.checkData(0, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 1000))
        tdSql.checkData(0, 1, 2.0)
        tdSql.checkData(0, 2, 'ct1')
        tdSql.checkData(1, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(1, 1, 4.0)
        tdSql.checkData(1, 2, 'ct1')
        tdSql.checkData(2, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 2000))
        tdSql.checkData(2, 1, 22.0)
        tdSql.checkData(2, 2, 'ct2')
        tdSql.checkData(3, 0, datetime.datetime(2022, 1, 20, 15, 10, 22, 4000))
        tdSql.checkData(3, 1, 44.0)
        tdSql.checkData(3, 2, 'ct2')

        tdSql.execute('drop database diffneg')
    def stop(self):
        tdSql.close()
        tdLog.success("%s successfully executed" % __file__)

tdCases.addWindows(__file__, TDTestCase())
tdCases.addLinux(__file__, TDTestCase())
