<%@ page contentType="text/html; charset=GBK" language="java" errorPage="" %>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<script type="text/javascript">
	function logintwo()
	{
		targetForm=document.forms[0];
		targetForm.action="loginPro";
		targetForm.submit();
	}
	function regist()
	{
		targetForm=document.forms[0];
		targetForm.action="registPro";
		targetForm.submit();
	}
</script>
<html>
  <head>
    <title>��¼ҳ��</title>
  </head>
  
  <body>
    <form action="*Pro" method="post">
<table align="center">
	<caption><h3>ͨ���</h3></caption>
	
	<tr>
		<td>�û�����<input type="text" name="username"/></td>
	</tr>
	<tr align="center">
		<td>
			<input type="submit" value="��¼" onclick="logintwo();"/>
			<input type="button" value="ע��" onclick="regist();"/>									
		</td>			
	</tr>
</table>
</form>
  </body>
</html>
