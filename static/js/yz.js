<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>show_verify</title>
    <script src="/static/js/jquery-1.12.4.min.js"></script>
    <script>
        $(function () {
            // 添加点击事件 鼠标浮动时变成小手
            $('#sp').css('cursor', 'pointer').click(function () {
                // 获取到图片的src路径  换一个新的路径   此代码相当与在原来的基础上增加数据
                $('#yzm').attr('src', $("#yzm").attr('src')+'?1')
            })
        })
    </script>
</head>
<body>
<form action="/verify_check2/" method="post">
    {% csrf_token %}
    请输入验证码：<input type="text" name="verify"><br>
    <img src="/verify_code/" alt="" id="yzm"><span id="sp">看不清,换一张</span><br>
    <input type="submit" value="提交">
</form>
</body>
</html>

模板Code