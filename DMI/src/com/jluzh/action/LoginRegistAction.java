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
	
	
	public String regist() throws Exception
	{
		setTip("¹§Ï²Äú×¢²á³É¹¦!");
		return SUCCESS;
	}
	
	public String loginone() throws Exception
	{
		if (getUsername().equals("chw"))
		{
			setTip("¹§Ï²ÄúµÇÂ½³É¹¦£¡");
			return SUCCESS;
		}	
			
		else
			return ERROR;
	}

}
