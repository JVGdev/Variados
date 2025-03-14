
package com.chess.pieces;
import com.boardgame.Board;
import com.chess.*;
import com.chess.pieces.*;

public class King extends ChessPiece{
	
	public King(Board board, Color color){
		super(board, color);
	}

	@Override
	public String toString(){
		return "K";
	}
	
} 
