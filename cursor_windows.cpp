#include <stdio.h>
#include <wchar.h>
#include <windows.h>

extern "C" {

	__declspec(dllexport)
		void setCursorPos(const short x, const short y) {
			SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), {x, y});
		}
		
	__declspec(dllexport)
		COORD getCursorPosition()   {
			CONSOLE_SCREEN_BUFFER_INFO info;
			GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
			return info.dwCursorPosition;
		}

	__declspec(dllexport)
		int getCursorX(){
			return getCursorPosition().X;
		}

	__declspec(dllexport)
		int getCursorY(){
			return getCursorPosition().Y;
		}

	__declspec(dllexport)
		void writeConsole(const char *string, const int length) {
			char *buffer = new char[length];
			for(int i = 0; i < length; i++)
				buffer[i] = string[i * 2];
			WriteConsole(GetStdHandle(STD_OUTPUT_HANDLE), buffer, length, nullptr, NULL);
		}

} // extern "C"
