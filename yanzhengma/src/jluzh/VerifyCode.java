package jluzh;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Random;

import javax.imageio.ImageIO;

public class VerifyCode {
	private int w = 70;
	private int h = 35;
 	private Random r = new Random();
 	// {"瀹嬩綋", "鍗庢枃妤蜂綋", "榛戜綋", "鍗庢枃鏂伴瓘", "鍗庢枃闅朵功", "寰蒋闆呴粦", "妤蜂綋_GB2312"}
	private String[] fontNames  = {"瀹嬩綋", "鍗庢枃妤蜂綋", "榛戜綋", "寰蒋闆呴粦", "妤蜂綋_GB2312"};
	// 鍙�夊瓧绗�
	private String codes  = "23456789abcdefghjkmnopqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ";
	// 鑳屾櫙鑹�
	private Color bgColor  = new Color(255, 255, 255);
	// 楠岃瘉鐮佷笂鐨勬枃鏈�
	private String text ;
	
	// 鐢熸垚闅忔満鐨勯鑹�
	private Color randomColor () {
		int red = r.nextInt(150);
		int green = r.nextInt(150);
		int blue = r.nextInt(150);
		return new Color(red, green, blue);
	}
	
	// 鐢熸垚闅忔満鐨勫瓧浣�
	private Font randomFont () {
		int index = r.nextInt(fontNames.length);
		String fontName = fontNames[index];//鐢熸垚闅忔満鐨勫瓧浣撳悕绉�
		int style = r.nextInt(4);//鐢熸垚闅忔満鐨勬牱寮�, 0(鏃犳牱寮�), 1(绮椾綋), 2(鏂滀綋), 3(绮椾綋+鏂滀綋)
		int size = r.nextInt(5) + 24; //鐢熸垚闅忔満瀛楀彿, 24 ~ 28
		return new Font(fontName, style, size);
	}
	
	// 鐢诲共鎵扮嚎
	private void drawLine (BufferedImage image) {
		int num  = 3;//涓�鍏辩敾3鏉�
		Graphics2D g2 = (Graphics2D)image.getGraphics();
		for(int i = 0; i < num; i++) {//鐢熸垚涓や釜鐐圭殑鍧愭爣锛屽嵆4涓��
			int x1 = r.nextInt(w);
			int y1 = r.nextInt(h);
			int x2 = r.nextInt(w);
			int y2 = r.nextInt(h); 
			g2.setStroke(new BasicStroke(1.5F)); 
			g2.setColor(Color.BLUE); //骞叉壈绾挎槸钃濊壊
			g2.drawLine(x1, y1, x2, y2);//鐢荤嚎
		}
	}
	
	// 闅忔満鐢熸垚涓�涓瓧绗�
	private char randomChar () {
		int index = r.nextInt(codes.length());
		return codes.charAt(index);
	}
	
	// 鍒涘缓BufferedImage
	private BufferedImage createImage () {
		BufferedImage image = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB); 
		Graphics2D g2 = (Graphics2D)image.getGraphics(); 
		g2.setColor(this.bgColor);
		g2.fillRect(0, 0, w, h);
 		return image;
	}
	
	// 璋冪敤杩欎釜鏂规硶寰楀埌楠岃瘉鐮�
	public BufferedImage getImage () {
		BufferedImage image = createImage();//鍒涘缓鍥剧墖缂撳啿鍖� 
		Graphics2D g2 = (Graphics2D)image.getGraphics();//寰楀埌缁樺埗鐜
		StringBuilder sb = new StringBuilder();//鐢ㄦ潵瑁呰浇鐢熸垚鐨勯獙璇佺爜鏂囨湰
		// 鍚戝浘鐗囦腑鐢�4涓瓧绗�
		for(int i = 0; i < 4; i++)  {//寰幆鍥涙锛屾瘡娆＄敓鎴愪竴涓瓧绗�
			String s = randomChar() + "";//闅忔満鐢熸垚涓�涓瓧姣� 
			sb.append(s); //鎶婂瓧姣嶆坊鍔犲埌sb涓�
			float x = i * 1.0F * w / 4; //璁剧疆褰撳墠瀛楃鐨剎杞村潗鏍�
			g2.setFont(randomFont()); //璁剧疆闅忔満瀛椾綋
			g2.setColor(randomColor()); //璁剧疆闅忔満棰滆壊
			g2.drawString(s, x, h-5); //鐢诲浘
		}
		this.text = sb.toString(); //鎶婄敓鎴愮殑瀛楃涓茶祴缁欎簡this.text
		drawLine(image); //娣诲姞骞叉壈绾�
		return image;		
	}
	
	// 杩斿洖楠岃瘉鐮佸浘鐗囦笂鐨勬枃鏈�
	public String getText () {
		return text;
	}
	
	// 淇濆瓨鍥剧墖鍒版寚瀹氱殑杈撳嚭娴�
	public static void output (BufferedImage image, OutputStream out) 
				throws IOException {
		ImageIO.write(image, "PNG", out);
	}
}


