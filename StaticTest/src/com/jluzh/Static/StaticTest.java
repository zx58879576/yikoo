package com.jluzh.Static;
/*
 * static��������������ͨ������ֱ����
 */
public class StaticTest {
	public static int t=4;
	static {t=30;
	System.out.println("t:"+t);	
	}
	
public static void AClass() {
	System.out.println("���Ǿ�̬A��");
}
public static void BClass() {
	AClass();
	System.out.println("���Ǿ�̬B��");
}
public void CClass() {
	System.out.println("������ͨC��");
}

@SuppressWarnings("static-access")
public static void main(String[] args) {
	StaticTest a=new StaticTest();
	AClass();
	
	a.BClass();
	a.CClass();
	
	
}
}
