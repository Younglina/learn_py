from mailFunc import send_email

"""发送邮件
:param from_user: 发件人
:param to_users: 收件人，多个收件人用英文分号进行分隔
:param subject: 邮件的主题
:param content: 邮件正文内容
:param filenames: 附件要发送的文件路径
"""
from_user='wy201904091002@qq.com'
to_users='wy201904091002@qq.com;1150382668@qq.com;1250407177@qq.com'
subject='哈哈哈嗯'
content='老得定制页面掉的主线接口，定制页面的密码框返回会有问题，测试提出bug的话，这个的解决就是跟主线同样处理方式，参考主线的代码https://aitrust-wikiailpha.dbappsecurity.com.cn/wiki/pages/viewpage.action?pageId=83121819'
filenames=['useMail/123.png']
send_email(from_user, to_users, subject, content, filenames)