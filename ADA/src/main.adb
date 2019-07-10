with Ada.Text_IO;

procedure Main is
txt : String;
begin
   --  Insert code here.
   Ada.Text_IO.Put_Line("Hello World !!! ");
   ada.Text_IO.Put_Line("Please enter some text and hit enter to view the same again --");
   txt := String'Image(Ada.Text_IO.Get_Line);
   null;
end Main;
