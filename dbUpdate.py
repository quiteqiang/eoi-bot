import sqlite3

db_file = 'test01.db'      # SQLite 数据库文件
table_name = 'eoi_test_01'         # 要导入的表名

# 修改测试数据
def updateDB():
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()

  sql_1 = f"""
  UPDATE {table_name}
  SET Occupation = 'Developer Programmer'
  WHERE  Occupation = 'DP'
  """
  print(sql_1)
  cursor.execute(sql_1)
  conn.commit()
  conn.close()

def updateDBMonth():
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()

  sql_1 = f"""
    UPDATE {table_name} SET Month = REPLACE(Month, "/", "-")
  """
  print(sql_1)
  cursor.execute(sql_1)
  conn.commit()
  conn.close()

def checkDB():
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()

  sql = "SELECT * FROM eoi_test_01 where Occupation == 'Developer Programmer'"
  cursor.execute(sql)
  rows = cursor.fetchall()
  for row in rows:
    print(row)

def checkDBByDate():
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()

  sql = "SELECT * FROM eoi_test_01 where Occupation == 'Developer Programmer' and Month between '2025-10' and '2026-11'  order by Month"
  cursor.execute(sql)
  rows = cursor.fetchall()
  for row in rows:
    print(row)

def schemaCheck():
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()
  # 获取表结构
  schema = cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
  print("******************************")
  for col in schema:
    print(col)
  print("******************************")

# updateDB()
# checkDB()
checkDBByDate()
# updateDBMonth()
# schemaCheck()