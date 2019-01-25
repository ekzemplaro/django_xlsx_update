from django.shortcuts import render

import os
import openpyxl
import pprint
from django.http import HttpResponse

def index(request):
    """
      Excel output from template
    """
    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook('/var/tmp/xlsx/cities.xlsx')

    sheet = wb['Cities']
    sheet['C4'] = '99999'
    sheet['D4'] = '2019-1-20'

# Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'report.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response
