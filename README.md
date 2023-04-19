# david-mysql-tools(Fit MySQL 8.0 & Python3)
在源代码的基础上稍加修改使其适应python3和mysql8.0

Modify the code to accommodate the mysql8.0  and python3, based on code.google.com/p/david-mysql-tools


## Key differences
- File Page Types Update（页类型的新增）
  - MySQL8.0 add new File Page Types which can found in its Source Code(/storage/innobase/include/fil0fil.h)
  - The inital table contains 7 pages(112K) in Mysql8. By contrast Mysql5.6 contains 6 pages(96K)
  
- The python3 syntax about `print`（`python3 print`格式更新）
