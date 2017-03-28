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
    
    func OLD_exec_post_request(user_data: Data){
        
        let url = NSURL(string: "http://localhost:8000/signup")!
        let request = NSMutableURLRequest(url: url as URL)
        request.httpMethod = "POST"
        
        request.httpBody = user_data
        
        let task = URLSession.shared.dataTask(with: request as URLRequest){ data,response,error in
            
            do {
                print(111)
                let json = try JSONSerialization.jsonObject(with: data!, options: .mutableContainers) as? NSDictionary
                print(json)
                if let parseJSON = json {
                    print(222)
                    let resultValue:String = parseJSON["success"] as! String;
                    print("result: \(resultValue)")
                    print(parseJSON)
                }
            } catch let error as NSError {
                print("in here")
                print(error)
            }
        }
        task.resume()
        
    }
    
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
    }
}

