package com.jluzh.Super;

public class SuperTest {
	public int a=1;
	private int b=2;
	protected int c=3;
public SuperTest() {
	this("he");
	// TODO Auto-generated constructor stub
System.out.println("���Ǹ��๹�췽��");
}
public SuperTest(String name) {
	
	System.out.println("���Ǹ����вι��췽��"+name);
}
public void sup() {
	String a=super.toString();
	// TODO Auto-generated method stub
System.out.println("���Ǹ�����ͨ����"+a);
}
public static void main(String[] args) {
SuperTest s=new SuperTest();
s.sup();

}
}
