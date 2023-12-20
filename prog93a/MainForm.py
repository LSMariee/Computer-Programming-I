import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
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
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.SaddleBrown
		self._label1.Location = System.Drawing.Point(61, 54)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(168, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Kilowatts used:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(295, 60)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(168, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SaddleBrown
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Linen
		self._button1.Location = System.Drawing.Point(12, 366)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(154, 57)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SaddleBrown
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Linen
		self._button2.Location = System.Drawing.Point(189, 366)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(154, 57)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SaddleBrown
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Linen
		self._button3.Location = System.Drawing.Point(359, 366)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(154, 57)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.SaddleBrown
		self._label2.Location = System.Drawing.Point(76, 115)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(168, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Base Rate:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.SaddleBrown
		self._label3.Location = System.Drawing.Point(76, 159)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(168, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Surcharge:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.SaddleBrown
		self._label4.Location = System.Drawing.Point(76, 206)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(168, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Citytax:"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.SaddleBrown
		self._label5.Location = System.Drawing.Point(76, 253)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(192, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Pay This Amount:"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.SaddleBrown
		self._label6.Location = System.Drawing.Point(76, 304)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(192, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "After May 20th Pay:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Peru
		self._label7.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.Linen
		self._label7.Location = System.Drawing.Point(295, 112)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(168, 32)
		self._label7.TabIndex = 10
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Peru
		self._label8.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Linen
		self._label8.Location = System.Drawing.Point(295, 156)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(168, 32)
		self._label8.TabIndex = 11
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Peru
		self._label9.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.Linen
		self._label9.Location = System.Drawing.Point(295, 250)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(168, 32)
		self._label9.TabIndex = 13
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Peru
		self._label10.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Linen
		self._label10.Location = System.Drawing.Point(295, 203)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(168, 32)
		self._label10.TabIndex = 12
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Peru
		self._label11.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.Linen
		self._label11.Location = System.Drawing.Point(295, 301)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(168, 32)
		self._label11.TabIndex = 14
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.BurlyWood
		self.ClientSize = System.Drawing.Size(525, 457)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog93a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		kilo = int(self._textBox1.Text)
		base = kilo * 0.0457
		base = round(base, 2)
		self._label7.Text = str(base)
		surcharge = base * 0.1
		surcharge = round(surcharge, 2)
		self._label8.Text = str(surcharge)
		utility = base * 0.03
		utility = round(utility, 2)
		self._label10.Text = str(utility)
		bill = base + surcharge + utility
		bill = round(bill, 2)
		self._label9.Text = str(bill)
		late = bill * 0.04
		penalty = late + bill
		penalty = round(penalty, 2)
		self._label11.Text = str(penalty)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label10.Text = ""
		self._label9.Text = ""
		self._label11.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()