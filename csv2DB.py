# Convert csv data into sqlite DB

import sqlite3
import csv

def csv2DB ():
  # 配置参数
  csv_file = 'au-eoi-data.csv'          # CSV 文件路径
  db_file = 'test01.db'      # SQLite 数据库文件
  table_name = 'eoi_test_01'         # 要导入的表名

  # 连接数据库（自动创建文件）
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()

  # 读取 CSV 第一行获取列名（假设第一行为标题）
  with open(csv_file, 'r', encoding='utf-8') as f:
      reader = csv.reader(f)
      headers = next(reader)      # 列名列表

  # 创建表（如果不存在），根据实际数据类型调整列定义
  # 这里暂时全部设为 TEXT，后续可按需转换
  columns = ', '.join([f'"{col}" TEXT' for col in headers])
  create_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'
  cursor.execute(create_sql)

  # 准备插入语句（使用占位符）
  placeholders = ', '.join(['?' for _ in headers])
  insert_sql = f'INSERT INTO {table_name} VALUES ({placeholders})'

  # 再次打开 CSV 并逐行插入（跳过标题行）
  with open(csv_file, 'r', encoding='utf-8') as f:
      reader = csv.reader(f)
      next(reader)                # 跳过标题行
      for row in reader:
          # 可在此处对 row 进行数据清洗/类型转换
          cursor.execute(insert_sql, row)

  # 提交并关闭
  conn.commit()
  conn.close()

  print(f"成功将 {csv_file} 导入到 {db_file} 的 {table_name} 表。")

def readDB(db_file):
    # 打开链接
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()
  sql = "SELECT * FROM eoi_test_01"
  cursor.execute(sql)
  rows = cursor.fetchall()
  for row in rows:
    print(row)

readDB("test01.db")