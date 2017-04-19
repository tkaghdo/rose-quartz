//
//  LoginViewController.swift
//  RoseQuartz
//
//  Created by Tamby Kaghdo on 4/4/17.
//  Copyright © 2017 Tamby Kaghdo. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    
    //MARK: Properties
    
    @IBOutlet weak var email: UITextField!
    @IBOutlet weak var password: UITextField!
    

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    //Mark: Actions
    @IBAction func login(_ sender: UIButton) {
        
        //TODO: encode the values
        
        let user_dict: [String:String] = [
            "email" : email.text!,
            "password" : password.text!
        ]
        
        
        // post user_dict to backend
        login_user(user: user_dict)
 
    }
    
    // MARK: helper methods
    
    func convertToDictionary(text: String) -> [String: Any]? {
        if let data = text.data(using: .utf8) {
            do {
                return try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any]
            } catch {
                print(error.localizedDescription)
            }
        }
        return nil
    }
    
    func navigate_to_next_screen(next_screen: String) {
        // go to langauge selection view
        //performSegue(withIdentifier: "LanguageSelectionSegue", sender: self)
        print("** NEXT SCREEN IS **: " + next_screen)
        if (next_screen == "GO_TO_LANGUAGE_SELECTION"){
            //performSegue(withIdentifier: "LanguageSelectionSegue", sender: self)
        }
        else{
            print("other screen")
        }
        
    }
    
    func login_user(user: [String:String]){
        
        let jsonData = try? JSONSerialization.data(withJSONObject: user, options: [])
        
        var request = URLRequest(url: URL(string: "http://localhost:8000/login")!)
        request.httpMethod = "POST"
        
        request.httpBody = jsonData
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else { // check for fundamental networking error
                print("error=\(error)")
                return
            }
            
            if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 201 { // user unable to login
                print("statusCode should be 201, but is \(httpStatus.statusCode)")
                print("response = \(response)")
            }
            else if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode == 201 { // user login success
                print("*login success*")
                print("login response = \(response)")
                
                let responseString = String(data: data, encoding: .utf8)
                print("responseString= \(responseString)")
                
                // forward user to select language
                // which screen should you go to
                //GO_TO_LANGUAGE_SELECTION or GO_TO_NEXT_QUESTION?
                
                let dict = self.convertToDictionary(text: responseString!)
                
                self.navigate_to_next_screen(next_screen: dict!["next_screen"] as! String)
                
            }
        }
        task.resume()
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
