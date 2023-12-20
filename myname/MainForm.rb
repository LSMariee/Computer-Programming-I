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
		@label1.BackColor = System::Drawing::Color.PeachPuff
		@label1.Font = System::Drawing::Font.new("Rockwell", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.SaddleBrown
		@label1.Location = System::Drawing::Point.new(149, 22)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(343, 150)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.DarkSalmon
		@button1.Font = System::Drawing::Font.new("Rockwell", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.PeachPuff
		@button1.Location = System::Drawing::Point.new(86, 239)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(182, 108)
		@button1.TabIndex = 1
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.LightSalmon
		@button2.Font = System::Drawing::Font.new("Rockwell", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.PeachPuff
		@button2.Location = System::Drawing::Point.new(377, 239)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(182, 105)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.AntiqueWhite
		self.ClientSize = System::Drawing::Size.new(635, 420)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "practice"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Lidia Sherfinski"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

