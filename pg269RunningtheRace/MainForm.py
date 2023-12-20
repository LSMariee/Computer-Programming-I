import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(39, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(336, 70)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the three runners' names and finishing times."
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(24, 140)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(94, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Runner 1:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(24, 183)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(94, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Runner 2:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(24, 227)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(94, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Runner 3:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(115, 137)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(116, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(115, 180)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(116, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(115, 221)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(116, 20)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(131, 111)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(54, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Name"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(282, 137)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(69, 20)
		self._textBox4.TabIndex = 8
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(282, 180)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(69, 20)
		self._textBox5.TabIndex = 9
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(282, 221)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(69, 20)
		self._textBox6.TabIndex = 10
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(269, 102)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(95, 32)
		self._label6.TabIndex = 11
		self._label6.Text = "Finishing time (in seconds)"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleVioletRed
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(24, 431)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 45)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate Results"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleVioletRed
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(157, 431)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 45)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleVioletRed
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(291, 431)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 45)
		self._button3.TabIndex = 14
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.NavajoWhite
		self._label7.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(24, 254)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(369, 160)
		self._label7.TabIndex = 15
		self._label7.Text = "Race Results"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.NavajoWhite
		self._label8.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(101, 280)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(71, 23)
		self._label8.TabIndex = 16
		self._label8.Text = "1st Place:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.White
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label9.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(203, 281)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(117, 20)
		self._label9.TabIndex = 17
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.NavajoWhite
		self._label10.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(101, 322)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(84, 23)
		self._label10.TabIndex = 18
		self._label10.Text = "2nd Place:"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.NavajoWhite
		self._label11.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(101, 363)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(71, 23)
		self._label11.TabIndex = 19
		self._label11.Text = "3rd Place:"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.White
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label12.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(203, 323)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(117, 20)
		self._label12.TabIndex = 20
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.White
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label13.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(203, 366)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(117, 20)
		self._label13.TabIndex = 21
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.AliceBlue
		self.ClientSize = System.Drawing.Size(417, 488)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg269SoftwareSales"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		runner1 = str(self._textBox1.Text)
		runner2 = str(self._textBox2.Text)
		runner3 = str(self._textBox3.Text)
		
		time1 = float(self._textBox4.Text)
		time2 = float(self._textBox5.Text)
		time3 = float(self._textBox6.Text)
		
		if time1 < time2 and time1 < time3 and time2 < time3:
			self._label9.Text = str(runner1)
			self._label12.Text = str(runner2)
			self._label13.Text = str(runner3)
		if time3 < time2 and time3 > time1:
			self._label9.Text = str(runner1)
			self._label12.Text = str(runner3)
			self._label13.Text = str(runner2)
		elif time2 > time3 and time2 < time1:
			self._label9.Text = str(runner3)
			self._label12.Text = str(runner2)
			self._label13.Text = str(runner1)
		elif time1 < time2 and time1 > time3:
			self._label9.Text = str(runner3)
			self._label12.Text = str(runner1)
			self._label13.Text = str(runner2)
		elif time1 > time2 and time1 > time3 and time2 < time3:
			self._label9.Text = str(runner2)
			self._label12.Text = str(runner3)
			self._label13.Text = str(runner1)
		elif time1 > time2 and time1 < time3:
			self._label9.Text = str(runner2)
			self._label12.Text = str(runner1)
			self._label13.Text = str(runner3)
			

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._textBox5.Text = ""
		self._textBox6.Text = ""
		self._label9.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()