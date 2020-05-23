Option Explicit

' Test the two loops
' View the results in the Immediate Window(Ctrl + G)
Sub TestLoops()

    'Dim dict As New Dictionary
    Dim dict As Object
    Set dict = CreateObject("Scripting.Dictionary")
    
    dict.Add "Apple", 5
    dict.Add "Orange", 7
    dict.Add "Peach", 13
    dict.Add "Pear", 23
    
    Debug.Print vbNewLine & "For Each"
    Call PrintDictionary(dict)
    
    Debug.Print vbNewLine & "For i"
    Call PrintDictionaryFor(dict)
    
End Sub

' Print the contents of the Dictionary to the Immediate Window(Ctrl + G) using For Each
Sub PrintDictionary(dict As Dictionary)

    Dim key As Variant
    For Each key In dict.Keys
        Debug.Print key, dict(key)
    Next

End Sub

' Print the contents of the Dictionary to the Immediate Window(Ctrl + G) using For i
Sub PrintDictionaryFor(dict As Dictionary)

    Dim i As Long
    For i = 0 To dict.Count - 1
        Debug.Print dict.Keys(i), dict.Items(i)
    Next i
    
End Sub


