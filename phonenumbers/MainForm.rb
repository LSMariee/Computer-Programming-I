require "mscorlib"
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
		@label1.BackColor = System::Drawing::Color.PaleVioletRed
		@label1.Font = System::Drawing::Font.new("Script MT Bold", 18, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.LavenderBlush
		@label1.Location = System::Drawing::Point.new(133, 55)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(399, 210)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Pink
		@button1.Font = System::Drawing::Font.new("Script MT Bold", 24, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.PaleVioletRed
		@button1.Location = System::Drawing::Point.new(79, 296)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(190, 111)
		@button1.TabIndex = 1
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Pink
		@button2.Font = System::Drawing::Font.new("Script MT Bold", 24, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.PaleVioletRed
		@button2.Location = System::Drawing::Point.new(392, 296)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(190, 111)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.LavenderBlush
		self.ClientSize = System::Drawing::Size.new(654, 434)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "phonenumbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Panera Bread(608)531-7097\n Earthsong (608)754-3933\n Havana Coffee (608)563-2970\n 608 Vintage (815)980-8427\n Bath & Body Works (608)758-8026"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

