package com.jluzh.action;

import com.opensymphony.xwork2.ActionSupport;

public class LoginRegistAction extends ActionSupport
{
	private String username;
	private String tip;
	
	public String getUsername()
	{
		return username;
	}
	public void setUsername(String username)
	{
		this.username=username;
	}
	
	public String getTip()
	{
		return tip;
	}
	public void setTip(String tip)
	{
		this.tip=tip;
	}
	
	public String login() throws Exception
	{
		if (getUsername().equals("chw"))
		{
			setTip("恭喜通过login()登录成功！");
			return SUCCESS;			
		}
			
		else
			return ERROR;
	}
	
	public String regist() throws Exception
	{
		setTip("恭喜通过regist()注册成功！");
		return SUCCESS;		
	}
	
	
	public String execute() throws Exception
	{
		if (getUsername().equals("chw"))
			return SUCCESS;
		else
			return ERROR;
	}

}
