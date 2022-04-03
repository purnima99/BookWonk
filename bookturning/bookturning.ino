
#include <Servo.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd( 7, 8, 9, 10, 11, 12);
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;
Servo myservo6;

void setup() 
{

  lcd.begin(16, 2);

  // left button
  pinMode(A0, INPUT);
  digitalWrite(A0 , HIGH);

  //right button
  pinMode(A1, INPUT);
  digitalWrite(A1, HIGH);

  myservo2.attach(2);
  myservo3.attach(3);
  myservo4.attach(4);
  myservo5.attach(5);
  myservo6.attach(6);

  myservo2.write(90);
  myservo3.write(0);
  myservo4.write(90);
  myservo5.write(90);
  myservo6.write(180);
  delay(3000);


  lcd.setCursor(0, 0);
  lcd.print("  BOOK WONK  ");
  delay(500);

  lcd.setCursor(0, 1);
  lcd.print("     PCPG54     ");
  delay(500);

  // attaches the servo on pin 9 to the servo object
}

void loop() 
{

  // left turn

  if (digitalRead(A0) == 0 )
  {

    lcd.setCursor(0, 1);
    lcd.print("  TURNING LEFT");
    delay(500);
    
    myservo2.write(90);
    myservo3.write(0);
    myservo4.write(90);
    myservo5.write(90);
    myservo6.write(180);

    //page holders
    myservo2.write(168);

    myservo4.write(17);
    delay(1000);
    
    //arm down
    myservo5.write(4);
    delay(3000);

    //wheel turn
    myservo6.write(0);
    delay(2000);

    //page hold left
    myservo2.write(90);
    delay(3000);

    //page flip
    myservo3.write(180);

    delay(3000);

    myservo2.write(90);
    myservo3.write(0);
    myservo4.write(90);
    myservo5.write(90);
    myservo6.write(180);

    lcd.setCursor(0, 1);
    lcd.print("                ");
    delay(500);

  }

  // right  turn

  if ( digitalRead(A1) == 0  )
  {
    lcd.setCursor(0, 1);
    lcd.print(" TURNING RIGHT");
    delay(500);
    myservo2.write(90);
    myservo3.write(180);
    myservo4.write(90);
    myservo5.write(90);
    myservo6.write(0);


    //page holders
    myservo2.write(168);

    myservo4.write(17);
    delay(1000);

    //arm down
    myservo5.write(176);
    delay(3000);


    //wheel turn
    myservo6.write(180);
    delay(2000);

    //page hold right
    myservo4.write(90);
    delay(3000);

    //page flip
    myservo3.write(0);
    delay(3000);



    myservo3.write(180);
    myservo2.write(90);
    myservo4.write(90);
    myservo5.write(90);
    myservo6.write(0);
    lcd.setCursor(0, 1);
    lcd.print("                ");
    delay(500);


  }



}
