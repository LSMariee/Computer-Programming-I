﻿require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LightSteelBlue
		@label1.Font = System::Drawing::Font.new("OCR A Extended", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.Lavender
		@label1.Location = System::Drawing::Point.new(166, 57)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(383, 179)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.LightSlateGray
		@button1.Font = System::Drawing::Font.new("OCR A Extended", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.Lavender
		@button1.Location = System::Drawing::Point.new(75, 278)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(219, 137)
		@button1.TabIndex = 1
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.LightSlateGray
		@button2.Font = System::Drawing::Font.new("OCR A Extended", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.Lavender
		@button2.Location = System::Drawing::Point.new(413, 278)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(219, 137)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Lavender
		self.ClientSize = System::Drawing::Size.new(709, 445)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "craigrules"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1. Text = "Craig Rules!"
	end

	def Button2Click(sender, e)
		@label1. Text = ""
	end
end

