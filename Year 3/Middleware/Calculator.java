import javax.swing.*;
import java.awt.*;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.awt.event.*;

public class Calculator extends JFrame {
	
	private static final long serialVersionUID = 1L;
	
	private JMenuBar menuBar;
	private JMenu file;
	private JMenu edit;
	private JMenuItem close;
	private JMenuItem copy;
	
	private JTextArea display;
	
	private JButton nine;
	private JButton eight;
	private JButton seven;
	private JButton six;
	private JButton five;
	private JButton four;
	private JButton three;
	private JButton two;
	private JButton one;
	private JButton zero;
	private JButton decimal;
	private JButton pi;
	
	private JButton clear;
	private JButton equals;
	private JButton add;
	private JButton mul;
	private JButton sub;
	private JButton div;

	private double tempFirst = 0.0;
	private double tempSecond = 0.0;

	private boolean[] operation = new boolean[4];

	public static void main (String[] arg) {
		new Calculator();
	}
	
	public Calculator(){
		super("Calculator");
		sendMenuBar();
		sendDisplay();
		sendButtons();
		sendUI(this);
	}

	private void sendMenuBar() {
		menuBar = new JMenuBar();
		file = new JMenu(" File ");
		edit = new JMenu(" Edit ");
		close = new JMenuItem("Close");
		copy = new JMenuItem("Copy");
		setJMenuBar(menuBar);
		menuBar.add(file);
		menuBar.add(edit);
		
		close.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		
		copy.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				String show = display.getText();
				StringSelection string = new StringSelection(show);
				Clipboard system = Toolkit.getDefaultToolkit().getSystemClipboard();
				system.setContents(string, string);
			}
		});	
		file.add(close);
		edit.add(copy);
	}
	
	private void sendDisplay() {
		display = new JTextArea("0");
		display.setBounds(10,10,290,50);
		display.setEditable(false);
		display.setFont(new Font("Century Gothic", Font.PLAIN, 20));
		add(display);
	}
	
	private void sendButtons() {
		add = new JButton("+");
		add.setBounds(235, 70, 65, 55);
		add.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				setTempFirst(Double.parseDouble(display.getText()));
				display.setText("0");
				operation[3] = true;
			}	
		});
		add(add);

		div = new JButton("/");
		div.setBounds(235, 135, 65, 55);
		div.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				setTempFirst(Double.parseDouble(display.getText()));
				display.setText("0");
				operation[0] = true;
			}	
		});
		add(div);

		mul = new JButton("*");
		mul.setBounds(235, 255, 65, 55);
		mul.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				setTempFirst(Double.parseDouble(display.getText()));
				display.setText("0");
				operation[1] = true;
			}	
		});
		add(mul);

		sub = new JButton("-");
		sub.setBounds(235, 195, 65, 55);
		sub.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				setTempFirst(Double.parseDouble(display.getText()));
				display.setText("0");
				operation[2] = true;
			}	
		});
		add(sub);

		clear = new JButton("Clear");
		clear.setBounds(160, 315, 140, 55);
		clear.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				display.setText("0");
				setTempFirst(0.0);
				setTempSecond(0.0);
				for (int i = 0; i <= 4; i++){
					operation[i] = false;
				}
			}	
		});
		add(clear);

		equals = new JButton("Calculate");
		equals.setBounds(10, 315, 140, 55);
		equals.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (operation[0]){
					System.out.println("HERE I AM");
					setTempSecond(Double.parseDouble(display.getText()));
					System.out.println(tempSecond);
					System.out.println(tempFirst);
					display.setText(Double.toString(getTempFirst() / getTempSecond()));
				}
				else if (operation[1]){
					setTempSecond(Double.parseDouble(display.getText()));
					display.setText(Double.toString(getTempFirst() * getTempSecond()));
				}
				else if (operation[2]){
					setTempSecond(Double.parseDouble(display.getText()));
					display.setText(Double.toString(getTempFirst() - getTempSecond()));
				}
				else if (operation[3]){
					setTempSecond(Double.parseDouble(display.getText()));
					display.setText(Double.toString(getTempFirst() + getTempSecond()));
				}
				if (display.getText().endsWith(".0")){
					display.setText(display.getText().replace(".0", ""));
				}
				setTempFirst(0.0);
				setTempSecond(0.0);
				for (int i = 0; i < 4; i++){
					operation[i] = false;
				}
			}	
		});
		add(equals);

		zero = new JButton("0");
		zero.setBounds(10, 255, 65, 55);
		zero.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().equalsIgnoreCase("0") || 
						display.getText().length() > 13) 
					return;
				display.append("0");
			}	
		});
		add(zero);
		decimal = new JButton(".");
		decimal.setBounds(85, 255, 65, 55);
		decimal.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13 ||
						display.getText().contains(".")) {
					return;
				}
				display.append(".");
			}	
		});
		add(decimal);

		pi = new JButton("pi");
		pi.setBounds(160, 255, 65, 55);
		pi.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				display.setText("3.14159265359");
			}	
		});
		add(pi);

		one = new JButton("1");
		one.setBounds(10, 195, 65, 55);
		one.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("1");
					return;
				}
				display.append("1");
			}	
		});

		add(one);
		two = new JButton("2");
		two.setBounds(85, 195, 65, 55);
		two.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("2");
					return;
				}
				display.append("2");
			}	
		});
		add(two);
		three = new JButton("3");
		three.setBounds(160, 195, 65, 55);
		three.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("3");
					return;
				}
				display.append("3");
			}	
		});
		add(three);
		four = new JButton("4");
		four.setBounds(10, 135, 65, 55);
		four.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("4");
					return;
				}
				display.append("4");
			}	
		});
		add(four);
		five = new JButton("5");
		five.setBounds(85, 135, 65, 55);
		five.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("5");
					return;
				}
				display.append("5");
			}	
		});
		add(five);
		six = new JButton("6");
		six.setBounds(160, 135, 65, 55);
		six.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("6");
					return;
				}
				display.append("6");
			}	
		});
		add(six);
		seven = new JButton("7");
		seven.setBounds(10, 70, 65, 55);
		seven.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("7");
					return;
				}
				display.append("7");
			}	
		});
		add(seven);
		eight = new JButton("8");
		eight.setBounds(85, 70, 65, 55);
		eight.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("8");
					return;
				}
				display.append("8");
			}	
		});
		add(eight);
		nine = new JButton("9");
		nine.setBounds(160, 70, 65, 55);
		nine.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (display.getText().length() > 13) {
					return;
				}
				if (display.getText().equalsIgnoreCase("0")) {
					display.setText("9");
					return;
				}
				display.append("9");
			}	
		});
		add(nine);	
	}

	private void sendUI(Calculator app) {
		app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		app.setSize(315, 420);
		app.setResizable(false);
		app.setLayout(null);
		app.setLocationRelativeTo(null);
		app.setVisible(true);
	}

	public double getTempFirst(){
		return tempFirst;
	}

	public void setTempFirst(double tempFirst){
		this.tempFirst = tempFirst;
	}

	public double getTempSecond(){
		return tempSecond;
	}

	public void setTempSecond (double tempSecond){
		this.tempSecond = tempSecond;
	}
}
