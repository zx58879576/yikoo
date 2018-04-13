package com.jluzh.Static;
/*
 * static方法及变量不用通过对象直接用
 */
public class StaticTest {
	public static int t=4;
	static {t=30;
	System.out.println("t:"+t);	
	}
	
public static void AClass() {
	System.out.println("我是静态A类");
}
public static void BClass() {
	AClass();
	System.out.println("我是静态B类");
}
public void CClass() {
	System.out.println("我是普通C类");
}

@SuppressWarnings("static-access")
public static void main(String[] args) {
	StaticTest a=new StaticTest();
	AClass();
	
	a.BClass();
	a.CClass();
	
	
}
}
