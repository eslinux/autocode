package mycompany;

import com.sun.jna.Callback;
import com.sun.jna.Library;
import com.sun.jna.Native;

public interface JNAApiInterface extends Library {
	@SuppressWarnings("deprecation")
	final JNAApiInterface INSTANCE = (JNAApiInterface) Native.loadLibrary("DLL3.dll", JNAApiInterface.class);

	float Add(float a, float b);

	float Sub(float a, float b);

	float Mul(float a, float b);

	float Dev(float a, float b);

	int initMyApp();

	// Define callback interface
	public interface foo extends Callback {
		void invoke(int a);
	}

	// define an implementation of the callback interface
	public static class fooCallbackImplementation implements foo {
		@Override
		public void invoke(int a) {
			System.out.println("foo callback: " + a);
		}
	}

	void setcb(int a, foo cb);

}