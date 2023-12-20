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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSteelBlue
		self._label1.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(23, 10)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(240, 160)
		self._label1.TabIndex = 0
		self._label1.Text = "Type of Membership"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSteelBlue
		self._label2.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(286, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(240, 160)
		self._label2.TabIndex = 1
		self._label2.Text = "Options"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSteelBlue
		self._label3.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(286, 179)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(240, 160)
		self._label3.TabIndex = 3
		self._label3.Text = "Membership Fees"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSteelBlue
		self._label4.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label4.Location = System.Drawing.Point(23, 180)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(240, 160)
		self._label4.TabIndex = 2
		self._label4.Text = "Membership Length"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSlateGray
		self._button1.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button1.Location = System.Drawing.Point(36, 377)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(142, 43)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSlateGray
		self._button2.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button2.Location = System.Drawing.Point(199, 377)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(142, 43)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightSlateGray
		self._button3.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button3.Location = System.Drawing.Point(366, 377)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(142, 43)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.LightSteelBlue
		self._radioButton1.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton1.Location = System.Drawing.Point(36, 41)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(187, 24)
		self._radioButton1.TabIndex = 7
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Standard Adult"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.LightSteelBlue
		self._radioButton2.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton2.Location = System.Drawing.Point(36, 71)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(213, 24)
		self._radioButton2.TabIndex = 8
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Child (12 and under)"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.LightSteelBlue
		self._radioButton3.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton3.Location = System.Drawing.Point(36, 101)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(213, 24)
		self._radioButton3.TabIndex = 9
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Student"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.Color.LightSteelBlue
		self._radioButton4.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton4.Location = System.Drawing.Point(36, 131)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(213, 24)
		self._radioButton4.TabIndex = 10
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senior Citizen"
		self._radioButton4.UseVisualStyleBackColor = False
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.LightSteelBlue
		self._checkBox1.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._checkBox1.Location = System.Drawing.Point(311, 43)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 11
		self._checkBox1.Text = "Yoga"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.LightSteelBlue
		self._checkBox2.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._checkBox2.Location = System.Drawing.Point(311, 71)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 12
		self._checkBox2.Text = "Karate"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.LightSteelBlue
		self._checkBox3.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._checkBox3.Location = System.Drawing.Point(311, 101)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(183, 24)
		self._checkBox3.TabIndex = 13
		self._checkBox3.Text = "Personal Trainer"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSteelBlue
		self._label5.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Location = System.Drawing.Point(36, 221)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(198, 39)
		self._label5.TabIndex = 14
		self._label5.Text = "Enter the Number of Months:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(58, 263)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(165, 20)
		self._textBox1.TabIndex = 15
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSteelBlue
		self._label6.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Location = System.Drawing.Point(311, 221)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(131, 27)
		self._label6.TabIndex = 16
		self._label6.Text = "Monthly Fee:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightSteelBlue
		self._label7.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label7.Location = System.Drawing.Point(365, 261)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(68, 27)
		self._label7.TabIndex = 17
		self._label7.Text = "Total:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label8.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(439, 224)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(69, 18)
		self._label8.TabIndex = 18
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label9.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(439, 263)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(69, 18)
		self._label9.TabIndex = 19
		# 
		# label10
		# 
		self._label10.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(211, 351)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(170, 23)
		self._label10.TabIndex = 20
		self._label10.Click += self.Label10Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Lavender
		self.ClientSize = System.Drawing.Size(544, 455)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._radioButton4)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg250membershipfee"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		months = int(self._textBox1.Text)
		price = 0
		price2 = 0
		price3 = 0
		
		
		
		if months < 0 or months > 24:
			MessageBox.Show("Invalid Number")
		
		if self._radioButton1.Checked == True:
			price = 40
		elif self._radioButton2.Checked == True:
			price = 20
		elif self._radioButton3.Checked == True:
			price = 25
		elif self._radioButton4.Checked == True:
			price = 30
			
		if self._checkBox1.Checked == True and self._checkBox2.Checked == False and self._checkBox3.Checked == False:
			price2 = price + 10
		elif self._checkBox2.Checked == True and self._checkBox1.Checked == False and self._checkBox3.Checked == False:
			price2 = price + 30
		elif self._checkBox3.Checked == True and self._checkBox2.Checked == False and self._checkBox1.Checked == False:
			price2 = price + 50
		else:
			price2 = price
		
		
		
			
		
		if months >=4 and months <=6:
			price3 = price2 * .05
			price4 = price2 - price3
		elif months >= 7 and months <= 9:
			price3 = price2 * .08
			price4 = price2 - price3
		elif months >= 10 and months < 25:
			price3 = price2 * 0.1
			price4 = price2 - price3
		else: 
			price3 = price2 + 0
			price4 = price3
		
		self._label8.Text = "$" + str(price4)
		self._label9.Text = "$" + str(months * price4)

	def Button2Click(self, sender, e):
		self._label10.Text = ""
		self._label9.Text = ""
		self._label8.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label10Click(self, sender, e):
		pass