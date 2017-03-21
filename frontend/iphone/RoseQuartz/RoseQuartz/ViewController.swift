//
//  ViewController.swift
//  RoseQuartz
//
//  Created by Tamby Kaghdo on 3/19/17.
//  Copyright © 2017 Tamby Kaghdo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: Properties
    
    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var emailTextField: UITextField!
    @IBOutlet weak var pwTextField: UITextField!
    
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    //MARK: Actions
    
    @IBAction func signup(_ sender: UIButton) {
        print("SIGN-UP PRESSED")
    }
}

