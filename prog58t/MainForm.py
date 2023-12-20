import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(117, 71)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(164, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(408, 71)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(164, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.RosyBrown
		self._label1.Location = System.Drawing.Point(117, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(152, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Purchase Price:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.RosyBrown
		self._label2.Location = System.Drawing.Point(408, 24)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(164, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Amount recieved:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.RosyBrown
		self._label3.Location = System.Drawing.Point(287, 94)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(117, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Change Due:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MistyRose
		self._label4.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.IndianRed
		self._label4.Location = System.Drawing.Point(242, 126)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(193, 35)
		self._label4.TabIndex = 5
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.RosyBrown
		self._label5.Location = System.Drawing.Point(77, 175)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(164, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "Dollars"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.RosyBrown
		self._label6.Location = System.Drawing.Point(77, 217)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(164, 23)
		self._label6.TabIndex = 7
		self._label6.Text = "Quarters:"
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.RosyBrown
		self._label7.Location = System.Drawing.Point(77, 260)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(164, 23)
		self._label7.TabIndex = 8
		self._label7.Text = "Dimes:"
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.RosyBrown
		self._label8.Location = System.Drawing.Point(77, 304)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(164, 23)
		self._label8.TabIndex = 9
		self._label8.Text = "Nickels:"
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.RosyBrown
		self._label9.Location = System.Drawing.Point(77, 346)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(164, 23)
		self._label9.TabIndex = 10
		self._label9.Text = "Pennies:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.MistyRose
		self._label10.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.IndianRed
		self._label10.Location = System.Drawing.Point(379, 173)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(193, 28)
		self._label10.TabIndex = 11
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.MistyRose
		self._label11.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.IndianRed
		self._label11.Location = System.Drawing.Point(379, 215)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(193, 28)
		self._label11.TabIndex = 12
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.MistyRose
		self._label12.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.IndianRed
		self._label12.Location = System.Drawing.Point(379, 258)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(193, 28)
		self._label12.TabIndex = 13
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.MistyRose
		self._label13.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.IndianRed
		self._label13.Location = System.Drawing.Point(379, 304)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(193, 28)
		self._label13.TabIndex = 14
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.MistyRose
		self._label14.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.IndianRed
		self._label14.Location = System.Drawing.Point(379, 344)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(193, 28)
		self._label14.TabIndex = 15
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.IndianRed
		self._button1.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.SeaShell
		self._button1.Location = System.Drawing.Point(52, 390)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(165, 60)
		self._button1.TabIndex = 16
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.IndianRed
		self._button2.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SeaShell
		self._button2.Location = System.Drawing.Point(258, 390)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(165, 60)
		self._button2.TabIndex = 17
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.IndianRed
		self._button3.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.SeaShell
		self._button3.Location = System.Drawing.Point(469, 390)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(165, 60)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Snow
		self.ClientSize = System.Drawing.Size(670, 462)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		price = float(self._textBox1.Text)
		recieved = float(self._textBox2.Text)
		change = recieved - price
		self._label4.Text = str(change)
		dollars = change // 1
		self._label10.Text = str(dollars)
		change2 = change - dollars
		quarters = change2 // 0.25
		self._label11.Text = str(quarters)
		change3 = change2 - quarters * 0.25
		dimes = change3 // 0.1
		self._label12.Text = str(dimes)
		change4 = change3 - dimes * 0.1
		nickels = change4 // 0.05
		self._label13.Text = str(nickels)
		change5 = change4 - nickels * 0.05
		pennies = change5 // 0.01
		self._label14.Text = str(pennies)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()