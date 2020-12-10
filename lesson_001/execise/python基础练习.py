'''从testerhome获取首页的代码，并统计有多少个帖子'''
'''1.curl https://testerhome.com | grep -E  ' <a title=".*" href=".*">.*</a>' | grep -v 'img' | wc -l
   2.curl https://testerhome.com | grep  ' <a title=".*" href=".*">[^<].*</a>' | wc -l
   3.curl https://testerhome.com | grep -E  ' <a title=".*" href="/(topics|articles).*">.*</a>' | wc -l
'''
'''curl https://testerhome.com |awk '/http:\/\/[a-zA-Z\\\.\\\-]*/'
 awk的用法：awk 'BEGIN{ print "start" } pattern{ commands } END{ print "end" }' file
 1.在一定程度上代替grep :curl https://testerhome.com |awk '/http:\/\/[a-zA-Z\\\.\\\-]*/'(必须使用转义\\\)
 2.awk表示正则匹配：'/xxx/' 
 3.awk表示区间选择：'/aa/,/bb/' :echo $PATH | awk 'BEGIN{RS=":"}{print $0}'| awk '/\/usr\/local\/bin/,/\/usr\/bin/'
 4.NR行数：echo $PATH |awk 'BEGIN{RS=":"}{print $0}'| awk 'NR==2'(取第2行)
 5.END结束：echo $PATH |awk 'BEGIN{RS=":"}{print $0}'| awk 'END{print NR}'
 6.$NF代表最后⼀个字段：echo $PATH |awk 'BEGIN{FS=":"}{print $NF}' 
 7.分隔符FS：awk -F =="BEGIN{FS=':'}"  不换行
 8.RS记录分隔符：BEGIN{RS=":"} 换行
 9.$0:代表当前记录;$1:代表第一个字段；
 10.OFS输出数据的字段分隔符：cat 3.txt | awk '{OFS="-"}{print $1,$2,$3}' (输出结果1-2-3)
11.修改OFS和ORS让$0重新计算 echo $PATH | awk 'BEGIN{FS=":";OFS=" | "}{$1=$1;print $0}'，如果不加$1=$1;则OFS不起作用
12.把单⾏分拆为多⾏：❖ echo $PATH | awk 'BEGIN{RS=":"}{print $0}'
❖ echo $PATH | awk 'BEGIN{RS=":"}{print NR,$0}'
❖ echo $PATH | awk 'BEGIN{RS=":"}END{print NR}'
13.多⾏组合为单⾏：echo $PATH | awk 'BEGIN{RS=":"}{print $0}' | awk 'BEGIN{ORS=":"}{print $0}'
 
 
 
 
 '''
