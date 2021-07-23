package mycompany;

import java.awt.EventQueue;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.SpringLayout;

import org.json.JSONArray;
import org.json.JSONObject;

import com.sun.jna.Memory;
import com.sun.jna.Pointer;
import com.sun.jna.ptr.PointerByReference;

public class Home {

	private JFrame frame;
	private JTextField textField_a;
	private JTextField textField_b;
	private ButtonGroup bg;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Home window = new Home();
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
	public Home() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 575, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		SpringLayout springLayout = new SpringLayout();
		frame.getContentPane().setLayout(springLayout);

//		if(false) {
//			JPanel panelmain = (JPanel) frame.getContentPane();
//	        JMenuBar menubar = new JMenuBar();
//	        JMenu fileMenu = new JMenu("File");
//	  
//	        JMenuItem about = new JMenuItem("About");
//	        about.addActionListener(new ActionListener()
//	        {
//	            @Override
//	            public void actionPerformed(ActionEvent e)
//	            {
//	                JOptionPane.showMessageDialog(
//	                		panelmain, 
//	                    "This is a modal MessageBox", 
//	                    "About", 
//	                    JOptionPane.INFORMATION_MESSAGE);
//	            }
//	        });
//	          
//	        fileMenu.add(about);
//	        menubar.add(fileMenu);
//	        frame.setJMenuBar(menubar);
//		}

		JLabel lblNewLabel = new JLabel("So a");
		springLayout.putConstraint(SpringLayout.NORTH, lblNewLabel, 42, SpringLayout.NORTH, frame.getContentPane());
		springLayout.putConstraint(SpringLayout.WEST, lblNewLabel, 39, SpringLayout.WEST, frame.getContentPane());
		frame.getContentPane().add(lblNewLabel);

		JLabel lblNewLabel_1 = new JLabel("So b");
		springLayout.putConstraint(SpringLayout.NORTH, lblNewLabel_1, 25, SpringLayout.SOUTH, lblNewLabel);
		springLayout.putConstraint(SpringLayout.WEST, lblNewLabel_1, 0, SpringLayout.WEST, lblNewLabel);
		frame.getContentPane().add(lblNewLabel_1);

		JLabel lblNewLabel_2 = new JLabel("Ket qua");
		springLayout.putConstraint(SpringLayout.NORTH, lblNewLabel_2, 58, SpringLayout.SOUTH, lblNewLabel_1);
		springLayout.putConstraint(SpringLayout.EAST, lblNewLabel_2, 0, SpringLayout.EAST, lblNewLabel);
		frame.getContentPane().add(lblNewLabel_2);

		textField_a = new JTextField();
		springLayout.putConstraint(SpringLayout.WEST, textField_a, 47, SpringLayout.EAST, lblNewLabel);
		springLayout.putConstraint(SpringLayout.SOUTH, textField_a, 0, SpringLayout.SOUTH, lblNewLabel);
		frame.getContentPane().add(textField_a);
		textField_a.setColumns(10);

		textField_b = new JTextField();
		springLayout.putConstraint(SpringLayout.WEST, textField_b, 0, SpringLayout.WEST, textField_a);
		springLayout.putConstraint(SpringLayout.SOUTH, textField_b, 0, SpringLayout.SOUTH, lblNewLabel_1);
		textField_b.setColumns(10);
		frame.getContentPane().add(textField_b);

		JPanel panel = new JPanel();
		springLayout.putConstraint(SpringLayout.NORTH, panel, 19, SpringLayout.SOUTH, textField_b);
		springLayout.putConstraint(SpringLayout.WEST, panel, 101, SpringLayout.WEST, frame.getContentPane());
		springLayout.putConstraint(SpringLayout.EAST, panel, -217, SpringLayout.EAST, frame.getContentPane());
		FlowLayout flowLayout = (FlowLayout) panel.getLayout();
		flowLayout.setAlignment(FlowLayout.LEFT);
		frame.getContentPane().add(panel);

		JRadioButton rdbtnAdd = new JRadioButton("Add");
		panel.add(rdbtnAdd);
		springLayout.putConstraint(SpringLayout.NORTH, rdbtnAdd, 23, SpringLayout.SOUTH, textField_b);
		springLayout.putConstraint(SpringLayout.EAST, rdbtnAdd, 0, SpringLayout.EAST, textField_a);

		JRadioButton rdbtnSub = new JRadioButton("Sub");
		panel.add(rdbtnSub);

		JRadioButton rdbtnMul = new JRadioButton("Mul");
		panel.add(rdbtnMul);

		JRadioButton rdbtnDev = new JRadioButton("Dev");
		panel.add(rdbtnDev);

		JLabel lblResult = new JLabel("0");
		springLayout.putConstraint(SpringLayout.SOUTH, panel, -8, SpringLayout.NORTH, lblResult);
		springLayout.putConstraint(SpringLayout.WEST, lblResult, 0, SpringLayout.WEST, textField_a);
		springLayout.putConstraint(SpringLayout.SOUTH, lblResult, 0, SpringLayout.SOUTH, lblNewLabel_2);
		frame.getContentPane().add(lblResult);

		JButton btnCal = new JButton("Calculate");
		btnCal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {

				try {
					float a = Float.parseFloat(textField_a.getText());
					float b = Float.parseFloat(textField_b.getText());
					float result = 0;

					if (rdbtnAdd.isSelected()) {
						result = JNAApiInterface.INSTANCE.Add(a, b);
						lblResult.setText(String.valueOf(result));
					} else if (rdbtnSub.isSelected()) {
						result = JNAApiInterface.INSTANCE.Sub(a, b);
						lblResult.setText(String.valueOf(result));
					} else if (rdbtnMul.isSelected()) {
						result = JNAApiInterface.INSTANCE.Mul(a, b);
						lblResult.setText(String.valueOf(result));
					} else if (rdbtnDev.isSelected()) {
						if (b != 0) {
							result = JNAApiInterface.INSTANCE.Dev(a, b);
							lblResult.setText(String.valueOf(result));
						} else {
							lblResult.setText("b invalid");
						}
					}
				} finally {
					// TODO: handle finally clause
				}
			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btnCal, 18, SpringLayout.SOUTH, lblResult);
		springLayout.putConstraint(SpringLayout.WEST, btnCal, 0, SpringLayout.WEST, textField_a);
		frame.getContentPane().add(btnCal);

		bg = new ButtonGroup();
		bg.add(rdbtnAdd);
		bg.add(rdbtnSub);
		bg.add(rdbtnMul);
		bg.add(rdbtnDev);
		rdbtnAdd.setSelected(true);

		JButton btnNewButton = new JButton("New button");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {

				// instantiate a callback wrapper instance
				final JNAApiInterface.fooCallbackImplementation callbackImpl = new JNAApiInterface.fooCallbackImplementation();

				// pass the callback wrapper to the C library
				JNAApiInterface.INSTANCE.setcb(1, callbackImpl);

			}
		});
		springLayout.putConstraint(SpringLayout.SOUTH, btnNewButton, -26, SpringLayout.SOUTH, frame.getContentPane());
		springLayout.putConstraint(SpringLayout.EAST, btnNewButton, -194, SpringLayout.EAST, frame.getContentPane());
		frame.getContentPane().add(btnNewButton);

		JButton btnOpenSqlite = new JButton("open sqlite");
		btnOpenSqlite.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {

				System.out.println("open sqlite: " + JNAApiInterface.INSTANCE.initMyApp());

			}
		});
		springLayout.putConstraint(SpringLayout.WEST, btnOpenSqlite, 30, SpringLayout.EAST, btnNewButton);
		springLayout.putConstraint(SpringLayout.SOUTH, btnOpenSqlite, 0, SpringLayout.SOUTH, btnNewButton);
		frame.getContentPane().add(btnOpenSqlite);

		JButton btnCPPCLI = new JButton("C++/CLI");
		btnCPPCLI.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {

//				System.out.println(JNA_CppCLIInterface.INSTANCE.Add(1, 2));
//				
//				
//				// instantiate a callback wrapper instance
//				final JNA_CppCLIInterface.fooCallbackImplementation callbackImpl2 = new JNA_CppCLIInterface.fooCallbackImplementation();
//				
//				// pass the callback wrapper to the C library
//				JNA_CppCLIInterface.INSTANCE.setcb(1, callbackImpl2);

				///
				JNA_CppCLIInterface.Example3Struct.ByReference e3ref = new JNA_CppCLIInterface.Example3Struct.ByReference();

				e3ref.listsong = new PointerByReference();
				
				e3ref.songname = "{" + "  \"geodata\": [" + "    {" + "      \"id\": \"1\","
						+ "      \"name\": \"Julie Sherman\"," + "      \"gender\" : \"female\","
						+ "      \"latitude\" : \"37.33774833333334\","
						+ "      \"longitude\" : \"-121.88670166666667\"" + "    }," + "    {" + "      \"id\": \"2\","
						+ "      \"name\": \"Johnny Depp\"," + "      \"gender\" : \"male\","
						+ "      \"latitude\" : \"37.336453\"," + "      \"longitude\" : \"-121.884985\"" + "    }"
						+ "  ]" + "}";

				JNA_CppCLIInterface.INSTANCE.example3_sendStruct(e3ref);
				System.out.println(e3ref.songname);

				// extract values
				final Pointer ex28p = e3ref.listsong.getValue();
				long ex28offset = 0;
				int ex28count = 0;
				while (ex28count < e3ref.valtest) {
					String s = ex28p.getString(ex28offset);
					System.out.println(s);
					ex28offset += s.length() + 1;
					ex28count++;
				}

			}
		});
		springLayout.putConstraint(SpringLayout.WEST, btnCPPCLI, 0, SpringLayout.WEST, btnOpenSqlite);
		springLayout.putConstraint(SpringLayout.SOUTH, btnCPPCLI, 0, SpringLayout.SOUTH, lblNewLabel_2);
		frame.getContentPane().add(btnCPPCLI);

		JButton btn_JSON = new JButton("JSON");
		btn_JSON.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
				
				

				final String JSON_DATA = "{" + "  \"geodata\": [" + "    {" + "      \"id\": \"1\","
						+ "      \"name\": \"Julie Sherman\"," + "      \"gender\" : \"female\","
						+ "      \"latitude\" : \"37.33774833333334\","
						+ "      \"longitude\" : \"-121.88670166666667\"" + "    }," + "    {" + "      \"id\": \"2\","
						+ "      \"name\": \"Johnny Depp\"," + "      \"gender\" : \"male\","
						+ "      \"latitude\" : \"37.336453\"," + "      \"longitude\" : \"-121.884985\"" + "    }"
						+ "  ]" + "}";

				final JSONObject obj = new JSONObject(JSON_DATA);
				final JSONArray geodata = obj.getJSONArray("geodata");
				final int n = geodata.length();
				for (int i = 0; i < n; ++i) {
					final JSONObject person = geodata.getJSONObject(i);
					System.out.println(person.getInt("id"));
					System.out.println(person.getString("name"));
					System.out.println(person.getString("gender"));
					System.out.println(person.getDouble("latitude"));
					System.out.println(person.getDouble("longitude"));
				}

			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btn_JSON, 53, SpringLayout.NORTH, frame.getContentPane());
		springLayout.putConstraint(SpringLayout.WEST, btn_JSON, 0, SpringLayout.WEST, btnOpenSqlite);
		frame.getContentPane().add(btn_JSON);
		
		JButton btn_setget = new JButton("set/get");
		btn_setget.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				long start = System.nanoTime();
				
				
				
				for(int i = 0; i < 1; i++) {
				
					String svalue = "{" + "  \"geodata\": [" + "    {" + "      \"id\": \"1\","
							+ "      \"name\": \"Julie Sherman\"," + "      \"gender\" : \"female\","
							+ "      \"latitude\" : \"37.33774833333334\","
							+ "      \"longitude\" : \"-121.88670166666667\"" + "    }," + "    {" + "      \"id\": \"2\","
							+ "      \"name\": \"Johnny Depp\"," + "      \"gender\" : \"male\","
							+ "      \"latitude\" : \"37.336453\"," + "      \"longitude\" : \"-121.884985\"" + "    }"
							+ "  ]" + "}";
					//JNA_CppCLIInterface.INSTANCE.set_params(123, svalue);
					
					final PointerByReference gvalue = new PointerByReference();
	//				Pointer  value_ = new Pointer(svalue.length()+100);
	//				value_.setString(0, svalue);
					
					
					//set value to dll
					Memory memory = new Memory(123);
					memory.setString(0, "aaaaaaaaaaaaaa");
					gvalue.setValue(memory);
					
					//call if
					JNA_CppCLIInterface.INSTANCE.get_params(123, gvalue);
					
					//get value from dll
					final String val = gvalue.getValue().getString(0);
					System.out.println(i + " get_params from dll: " + val);
				
					
				}
				
//				float a = 1;
//				float b = 2;
//				System.out.println(JNA_CppCLIInterface.INSTANCE.Add(a, b));
				
				// ...
				long finish = System.nanoTime();
				long timeElapsed = finish - start;
				System.out.println("Total time duration: " + timeElapsed);
			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btn_setget, 23, SpringLayout.NORTH, frame.getContentPane());
		springLayout.putConstraint(SpringLayout.EAST, btn_setget, 0, SpringLayout.EAST, panel);
		frame.getContentPane().add(btn_setget);
		
		JButton btn_xml = new JButton("XML");
		btn_xml.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
				JNA_CppCLIInterface.INSTANCE.testXML();
				
				
			}
		});
		springLayout.putConstraint(SpringLayout.NORTH, btn_xml, 0, SpringLayout.NORTH, btn_setget);
		springLayout.putConstraint(SpringLayout.EAST, btn_xml, 0, SpringLayout.EAST, btnOpenSqlite);
		frame.getContentPane().add(btn_xml);

		JMenuBar menuBar = new JMenuBar();
		frame.setJMenuBar(menuBar);

		JMenu mnNewMenu = new JMenu("File");
		menuBar.add(mnNewMenu);

		JMenuItem mntm_open = new JMenuItem("Open");
		mntm_open.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {

				JOptionPane.showMessageDialog(frame.getContentPane(), "This is a modal MessageBox", "About",
						JOptionPane.INFORMATION_MESSAGE);
			}
		});
		mnNewMenu.add(mntm_open);

		JMenuItem mntm_close = new JMenuItem("close");
		mnNewMenu.add(mntm_close);

	}
}
