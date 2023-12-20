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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
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
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkKhaki
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.LemonChiffon
		self._label1.Location = System.Drawing.Point(12, 25)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(278, 212)
		self._label1.TabIndex = 0
		self._label1.Text = "Tickets Sold"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkKhaki
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.LemonChiffon
		self._label2.Location = System.Drawing.Point(305, 25)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(278, 212)
		self._label2.TabIndex = 1
		self._label2.Text = "Revenue Generated"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkKhaki
		self._label3.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.LemonChiffon
		self._label3.Location = System.Drawing.Point(22, 61)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(247, 36)
		self._label3.TabIndex = 2
		self._label3.Text = "Enter the number of tickets sold for each class of seats."
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(139, 116)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkKhaki
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.LemonChiffon
		self._label4.Location = System.Drawing.Point(53, 116)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(68, 20)
		self._label4.TabIndex = 4
		self._label4.Text = "Class A:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(139, 156)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(139, 195)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkKhaki
		self._label5.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.LemonChiffon
		self._label5.Location = System.Drawing.Point(53, 156)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(68, 20)
		self._label5.TabIndex = 7
		self._label5.Text = "Class B:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkKhaki
		self._label6.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.LemonChiffon
		self._label6.Location = System.Drawing.Point(53, 195)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(68, 20)
		self._label6.TabIndex = 8
		self._label6.Text = "Class C:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LemonChiffon
		self._button1.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DarkOliveGreen
		self._button1.Location = System.Drawing.Point(22, 283)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(148, 43)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate Revenue"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LemonChiffon
		self._button2.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DarkOliveGreen
		self._button2.Location = System.Drawing.Point(222, 283)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(146, 43)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LemonChiffon
		self._button3.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DarkOliveGreen
		self._button3.Location = System.Drawing.Point(417, 283)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(149, 43)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkKhaki
		self._label7.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.LemonChiffon
		self._label7.Location = System.Drawing.Point(364, 61)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(61, 20)
		self._label7.TabIndex = 12
		self._label7.Text = "Class A:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkKhaki
		self._label8.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.LemonChiffon
		self._label8.Location = System.Drawing.Point(364, 104)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(61, 20)
		self._label8.TabIndex = 13
		self._label8.Text = "Class B:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkKhaki
		self._label9.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.LemonChiffon
		self._label9.Location = System.Drawing.Point(364, 144)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(61, 20)
		self._label9.TabIndex = 14
		self._label9.Text = "Class C:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkKhaki
		self._label10.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.LemonChiffon
		self._label10.Location = System.Drawing.Point(318, 183)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(107, 20)
		self._label10.TabIndex = 15
		self._label10.Text = "Total Revenue:"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label11.Location = System.Drawing.Point(445, 63)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 20)
		self._label11.TabIndex = 16
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label12.Location = System.Drawing.Point(445, 104)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 20)
		self._label12.TabIndex = 17
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label13.Location = System.Drawing.Point(445, 144)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 20)
		self._label13.TabIndex = 18
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label14.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label14.Location = System.Drawing.Point(445, 183)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 20)
		self._label14.TabIndex = 19
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleGoldenrod
		self.ClientSize = System.Drawing.Size(595, 366)
		self.Controls.Add(self._label14)
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
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg186stadiumseating"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		A = float(self._textBox1.Text)
		B = float(self._textBox2.Text)
		C = float(self._textBox3.Text)
		Arev = A * 15
		Brev = B * 12
		Crev = C * 9
		total = Arev + Brev + Crev
		self._label11.Text = "$" + str(Arev)
		self._label12.Text = "$" + str(round(Brev, 2))
		self._label13.Text = "$" + str(round(Crev, 2))
		self._label14.Text = "$" + str(round(total, 2))

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()