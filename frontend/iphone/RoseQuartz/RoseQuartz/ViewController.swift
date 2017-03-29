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
    
    
    // MARK: helper methods
    
    func get_request(){
        let url = URL(string: "http://localhost:8000/signup/tamby")
        
        let task = URLSession.shared.dataTask(with: url!) { data, response, error in
            guard error == nil else {
                print(error!)
                return
            }
            guard let data = data else {
                print("Data is empty")
                return
            }
            
            let json = try! JSONSerialization.jsonObject(with: data, options: [])
            print(json)
        }
        
        task.resume()
    }
    
    // post
    func add_user(user: [String:String]){
        
        let jsonData = try? JSONSerialization.data(withJSONObject: user, options: [])
        
        var request = URLRequest(url: URL(string: "http://localhost:8000/signup")!)
        request.httpMethod = "POST"
        
        request.httpBody = jsonData
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else { // check for fundamental networking error
                print("error=\(error)")
                return
            }
            
            if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 201 { // user unable to signup
                print("statusCode should be 201, but is \(httpStatus.statusCode)")
                print("response = \(response)")
            }
            else if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode == 201 { // user signup success
                print("*signup success*")
                print("response = \(response)")
                // forward user to select language
            }
            
            
            let responseString = String(data: data, encoding: .utf8)
            print("responseString = \(responseString)")
        }
        task.resume()
    }
    
    
    //MARK: Actions
    
    
    @IBAction func signup(_ sender: UIButton) {
        
        //TODO: encode the values
        let user_dict: [String:String] = [
            "name" : nameTextField.text!,
            "email" : emailTextField.text!,
            "password" : pwTextField.text!
        ]
        
        // test get request
        // get_request()
        
        // TODO: post user_dict to backend
        
        add_user(user: user_dict)
    }
}

