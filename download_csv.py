import boto3
import csv
from datetime import datetime
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からテーブル名を取得
table_name = os.getenv('TABLE_NAME')

# DynamoDBに接続
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# データを取得
response = table.scan()

# data ディレクトリがなければ作成
if not os.path.exists('data'):
    os.makedirs('data')

# CSVファイルに保存するパスを設定
filename = f"data/data_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # ヘッダーを書く
    writer.writerow(response['Items'][0].keys())
    # データを書く
    for item in response['Items']:
        writer.writerow(item.values())

print(f"CSVファイル保存完了: {filename}")
