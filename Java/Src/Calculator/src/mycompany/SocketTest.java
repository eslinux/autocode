package mycompany;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.BorderLayout;
import javax.swing.SpringLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class SocketTest {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					SocketTest window = new SocketTest();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public SocketTest() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		SpringLayout springLayout = new SpringLayout();
		frame.getContentPane().setLayout(springLayout);
		
		JButton btnNewButton = new JButton("StartSocket");
		springLayout.putConstraint(SpringLayout.EAST, btnNewButton, 168, SpringLayout.WEST, frame.getContentPane());
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			
				JNA_CppCLIInterface.INSTANCE.startSocket();
			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btnNewButton, 35, SpringLayout.NORTH, frame.getContentPane());
		springLayout.putConstraint(SpringLayout.WEST, btnNewButton, 25, SpringLayout.WEST, frame.getContentPane());
		frame.getContentPane().add(btnNewButton);
		
		JButton btnStartsocket2 = new JButton("StartSocket2");
		btnStartsocket2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
				JNA_CppCLIInterface.INSTANCE.startSocket2();
			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btnStartsocket2, 19, SpringLayout.SOUTH, btnNewButton);
		springLayout.putConstraint(SpringLayout.WEST, btnStartsocket2, 0, SpringLayout.WEST, btnNewButton);
		springLayout.putConstraint(SpringLayout.EAST, btnStartsocket2, 131, SpringLayout.WEST, btnNewButton);
		frame.getContentPane().add(btnStartsocket2);
		
		JButton btn_startapp = new JButton("Start  app");
		btn_startapp.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
				JNA_CppCLIInterface.INSTANCE.startApp();
				
			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btn_startapp, 25, SpringLayout.SOUTH, btnStartsocket2);
		springLayout.putConstraint(SpringLayout.WEST, btn_startapp, 25, SpringLayout.WEST, frame.getContentPane());
		frame.getContentPane().add(btn_startapp);
		
		JButton btn_closeapp = new JButton("Close app");
		btn_closeapp.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				JNA_CppCLIInterface.INSTANCE.closeApp();
			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btn_closeapp, 11, SpringLayout.SOUTH, btn_startapp);
		springLayout.putConstraint(SpringLayout.WEST, btn_closeapp, 0, SpringLayout.WEST, btnNewButton);
		frame.getContentPane().add(btn_closeapp);
	}
}
