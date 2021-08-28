package mycompany;

import java.util.Arrays;
import java.util.List;

import com.sun.jna.Callback;
import com.sun.jna.Library;
import com.sun.jna.Native;
import com.sun.jna.Structure;
import com.sun.jna.ptr.PointerByReference;

public interface JNA_CppCLIInterface extends Library {
	@SuppressWarnings("deprecation")
	final JNA_CppCLIInterface INSTANCE = (JNA_CppCLIInterface) Native.loadLibrary("ClassLibrary_CLI.dll",
			JNA_CppCLIInterface.class);

	float Add(float a, float b);

	// Define callback interface
	public interface foo extends Callback {
		void invoke(int a);
	}

	// define an implementation of the callback interface
	public static class fooCallbackImplementation implements foo {
		@Override
		public void invoke(int a) {
			System.out.println("JNA_CppCLIInterface foo callback: " + a);
		}
	}

	void setcb(int a, foo cb);

	// ---
	public static class Example3Struct extends Structure {
		public int valtest;
		public String songname;
		public PointerByReference listsong;

		public static class ByReference extends Example3Struct implements Structure.ByReference {
		}

		@Override
		protected List getFieldOrder() {
			return Arrays.asList(new String[] { "valtest", "songname", "listsong" });
		}

	}

	// unless otherwise specified, ByReference is assumed - but it can't hurt to be
	// explicit
	public void example3_sendStruct(Example3Struct.ByReference sval);
	
	//
	int set_params(int id, String value);
	int get_params(int id, PointerByReference  value);
//	
	
	void startSocket();
	void startSocket2();
	
	
	void startApp();
	void closeApp();
	
	void testXML();
}
