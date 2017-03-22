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
        
        //TODO: encode the values
        let userDict: [String:String] = [
            "name" : nameTextField.text!,
            "email" : emailTextField.text!,
            "password" : pwTextField.text!
        ]
        // create the user json
        do {
            let jsonData = try JSONSerialization.data(withJSONObject: userDict, options: .prettyPrinted)
            // here "jsonData" is the dictionary encoded in JSON data
            
            
            // write the the json to file
            let file = "qqqq.txt" //this is the file. we will write to and read from it
            
            print(jsonData)
            let text = jsonData //just a tex
            
            if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
                //writing
                do {
                    print(dir)
                    let path = dir.appendingPathComponent(file)
                    try text.write(to: path)
                    print("***")
                }
                catch {print(error)}
                defer{} //TODO: delete json file
            }
            
        }
        catch {
            print(error)
        }
        
        
        /*
        if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            //writing
            do {
                print(dir)
                let path = dir.appendingPathComponent(file)
                try text.write(to: path, atomically: false, encoding: String.Encoding.utf8)
                print("***")
            }
            catch {print(error)}
            //TODO: delete json file
            defer{}
        }
        */
    }
}

