import os
import datetime


def main(datas, page=1):
    today = datetime.date.today()
    filename = "%d_%d_" % (today.month, today.day) + 'page%s' % page
    fout = open('%s.html' % filename, 'w', encoding='utf-8')
    fout.write('<html>')
    fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")  # 解决乱码
    fout.write('<body>')
    for data in datas:
        fout.write('<article>')
        fout.write('<a href=%s>%s</a>' % (data[1], data[0]))
        fout.write('<img src=%s height="691" width="464" />' % data[2])
        fout.write('<td><a href=%s>百度云链接,提取码：%s</a></td>' % (data[3], data[4]))
        if data[5] != None:
            fout.write('<td>磁力链接为:%s</td>' % data[5])
        fout.write('</article>')
    fout.write('</body>')
    fout.write('</html>')
    fout.close()
    print('成功爬取第%s页' % page)
