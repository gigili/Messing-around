<?php

class UserTest extends \PHPUnit_Framework_TestCase {

	protected $user;

	public function setUp(){
		$this->user =  new \App\Models\User;
	}

	/** @test */
	public function that_we_can_get_the_first_name(){

		$this->user->setFirstName("Igor");

		$this->assertEquals($this->user->getFirstName(), "Igor");
	}

	/** @test */
	public function that_we_can_get_the_last_name(){
		#$user = new \App\Models\User;

		$this->user->setLastName("Ilic");

		$this->assertEquals($this->user->getLastName(), "Ilic");
	}

	/** @test */
	public function that_the_full_name_is_returned(){
		#$user = new \App\Models\User;

		$this->user->setFirstName("Igor");
		$this->user->setLastName("Ilic");

		$this->assertEquals($this->user->getFullName(), "Igor Ilic");
	}

	public function testFirstAndLastNameAreTrimmed(){
		$user = new \App\Models\User;

		$user->setFirstName("Igor     ");
		$user->setLastName("    Ilic");

		$this->assertEquals($user->getFirstName(), "Igor");
		$this->assertEquals($user->getLastName(), "Ilic");
	}

	public function testEmailAddressCanBeSet(){
		#$user = new \App\Models\User;

		$email = "test@test.com";

		$this->user->setEmail($email);

		$this->assertEquals($this->user->getEmail(), $email);
	}


	public function testEmailVariablesContainCorrectValues() {
		$user = new \App\Models\User;

		$user->setFirstName("Igor");
		$user->setLastName("Ilic");
		$user->setEmail("test@test.com");

		$emailVariables = $user->getEmailVariables();

		$this->assertArrayHasKey("full_name", $emailVariables);
		$this->assertArrayHasKey("email", $emailVariables);


		$this->assertEquals($emailVariables['full_name'], "Igor Ilic");
		$this->assertEquals($emailVariables['email'], "test@test.com");
	}
}
