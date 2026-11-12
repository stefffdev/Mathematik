// Rendert PDF-Seiten als JPG (für große Scans, die als Ganzes zu groß sind).
// Bauen:  swiftc -O tools/render.swift -o tools/render
// Nutzen: tools/render <datei.pdf> <ausgabe-präfix> <skala> [seite]
import PDFKit
import AppKit

let a = CommandLine.arguments
guard a.count >= 4, let doc = PDFDocument(url: URL(fileURLWithPath: a[1])), let scale = Double(a[3]) else {
    print("usage: render <pdf> <outprefix> <scale> [page]"); exit(1)
}
print("pages: \(doc.pageCount)")
let pages: [Int] = a.count > 4 ? [Int(a[4])! - 1] : Array(0..<doc.pageCount)
for i in pages {
    guard let p = doc.page(at: i) else { continue }
    let r = p.bounds(for: .mediaBox)
    let w = Int(r.width * scale), h = Int(r.height * scale)
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8,
                               samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                               colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    let ctx = NSGraphicsContext(bitmapImageRep: rep)!
    NSGraphicsContext.current = ctx
    let cg = ctx.cgContext
    cg.setFillColor(NSColor.white.cgColor); cg.fill(CGRect(x: 0, y: 0, width: w, height: h))
    cg.scaleBy(x: scale, y: scale)
    p.draw(with: .mediaBox, to: cg)
    NSGraphicsContext.restoreGraphicsState()
    let data = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.8])!
    try! data.write(to: URL(fileURLWithPath: "\(a[2])_\(i + 1).jpg"))
}
