#include "mh-lcd.c"
#include "mh-uart.c"
#include "mh-utils.c"
int main(void)
{
uint8_t data;
 
lcd_init();
uart_init(38400);
DDRB =255;
for(;;)
  {
    data = uart_recv_byte();
switch(data)
	{
		case '1':PORTB=1;break;
		case '0':PORTB=0;break;
	}
  }
}
