import cv2
import numpy as np
import pytesseract
from imutils.perspective import four_point_transform
from imutils import contours

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    return edged

def find_document_contour(edged_image):
    cnts = cv2.findContours(edged_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    
    document_contour = None
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        
        if len(approx) == 4:
            document_contour = approx
            break
    
    return document_contour

def scan_document(image):
    edged = preprocess_image(image)
    document_contour = find_document_contour(edged)
    
    if document_contour is not None:
        transformed = four_point_transform(image, document_contour.reshape(4, 2))
        transformed_gray = cv2.cvtColor(transformed, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(transformed_gray)
        return text
    else:
        return "No se encontró un documento válido."

def main():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow("Escáner de Documentos", frame)
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            scanned_text = scan_document(frame)
            print("Texto escaneado:")
            print(scanned_text)
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
