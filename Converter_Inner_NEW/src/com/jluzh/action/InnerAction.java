package com.jluzh.action;

import java.util.Date;

import com.opensymphony.xwork2.ActionSupport;

public class InnerAction extends ActionSupport
{
	private int age;
	private double password;
	//private String password;
	private Date birth;
	
	//�޲����Ĺ�����
//	public InnerAction()
//	{
//		
//	}
	
	//��ʼ��ȫ�����ԵĹ�����
//	public InnerAction(int age,double password,Date birth)
//	{
//		this.age=age;
//		this.password=password;
//		this.birth=birth;
//		
//	}
	
//	public InnerAction(int age, String password, Date birth) {
//		super();
//		this.age = age;
//		this.password = password;
//		this.birth = birth;
//	}	
	
	public int getAge()
	{
		return age;
	}	

	public void setAge(int age)
	{
		this.age=age;
	}
	
	public double getPassword()
	{
		return password;
	}
	public void setPassword(double password)
	{
		this.password=password;
	}
	
//	public String getPassword() {
//		return password;
//	}
//	public void setPassword(String password) {
//		this.password = password;
//	}

	public void setBirth(Date birth)
	{
		this.birth=birth;
	}
	
	public Date getBirth()
	{
		return birth;
	}

	
	public String execute() throws Exception
	{
//		int age=this.getAge();
//		setAge(age+5);
		setAge(getAge()+5);
		//setPassword(getPassword()+10);
		return SUCCESS;
	}
}
