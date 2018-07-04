package com.jluzh.action;

import java.util.Map;

import com.opensymphony.xwork2.ActionSupport;

public class OGNLtoMapAction extends ActionSupport{
	private Map<String,User> user;
	
		
	public Map<String, User> getUser() {
		return user;
	}

	public void setUser(Map<String, User> user) {
		this.user = user;
	}


	@Override
	public String execute() throws Exception {
		if(getUser().get("small").getName().equals("chw"))
		{
			user.get("small").setAge(user.get("small").getAge()+10);
			//getUser().get("small").setAge(getUser().get("small").getAge()+10);
			return SUCCESS;
		}
		else
			return ERROR;
	}

}
